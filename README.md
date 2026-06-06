# Cold Email Campaign Tool

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

A production Streamlit application for running cold email campaigns at scale: upload a recipient list, compose once, attach a PDF, and send through your own SMTP account with live delivery tracking.

**Live deployment:** [bulk-email.streamlit.app](https://bulk-email.streamlit.app/)

## Overview

The tool removes the manual work from bulk outreach. Campaigns run directly against the sender's own email provider over SMTP (STARTTLS), so there is no third-party sending service, no stored credentials, and no data leaving the session. Recipient lists are parsed from plain CSV/TXT files, sends are rate-limited with a configurable delay to stay under provider spam thresholds, and every send is reported individually with success/failure metrics and per-recipient error detail.

The application is a single-file Streamlit app deployed on Streamlit Community Cloud; a scheduled keep-alive script prevents the hosted instance from sleeping.

## Key Features

- Multi-provider SMTP support: Gmail, Outlook, Yahoo, or any custom SMTP server and port
- Recipient lists from `.txt` or `.csv`, accepting both comma-separated and line-separated formats with basic address validation
- Optional PDF attachment, handled through a temporary file and deleted after the campaign completes
- Configurable inter-send delay (0-10 seconds) to avoid tripping provider rate limits
- Live progress bar with per-recipient send status during the campaign
- Post-campaign metrics: successful, failed, and total counts plus a per-recipient error report
- Email preview before sending
- In-app setup instructions for generating app passwords (Gmail, Outlook, Yahoo)
- Credentials are used in-session only; passwords are never stored or logged

## How It Works

```
recipient file (.txt/.csv) --> parse + validate
email body + subject + PDF --> MIME message per recipient
SMTP (STARTTLS, port 587)  --> provider --> recipients
                                |
                          live progress + results
```

A single SMTP connection is opened per campaign and reused for every recipient. Each message is assembled as a MIME multipart (plain-text body plus optional base64-encoded PDF part), sent, and recorded. Failures are caught per recipient so one bad address never aborts the rest of the run.

## Tech Stack

- Streamlit (UI, progress reporting, file uploads)
- Python standard library: `smtplib`, `email.mime`, `tempfile`
- Streamlit Community Cloud (hosting)

## Getting Started

### Prerequisites

- Python 3.7+
- An email account with SMTP access (Gmail and Yahoo require an app password)

### Run Locally

```bash
git clone https://github.com/iampreetdave-max/bulk-email.git
cd bulk-email
pip install streamlit
streamlit run app.py
```

Open `http://localhost:8501`, configure your provider and credentials, upload a recipient list, and send.

### Deploy

Push to GitHub and create a new app on [share.streamlit.io](https://share.streamlit.io) pointing at `app.py`. No environment variables are required; credentials are entered at runtime in the UI.

## Provider Notes

| Provider | Requirement |
|----------|-------------|
| Gmail | 2-Step Verification + app password (regular password will not work) |
| Outlook | App password from account security settings |
| Yahoo | App password from account security settings |
| Other | SMTP server hostname and port (587 TLS typical) |

## Operational Guidance

- Test with a small batch (5-10 recipients) before a full run
- Keep a 1-2 second delay between sends; new accounts have lower sending limits
- Comply with CAN-SPAM, GDPR, and your provider's bulk-sending policies

## Project Structure

```
bulk-email/
├── app.py               # Streamlit application: SMTP config, parsing, sending, reporting
├── login_script.py      # Keep-alive helper for the hosted deployment
├── .github/workflows/   # Scheduled automation
├── LICENSE
└── README.md
```

## License

See [LICENSE](LICENSE).
