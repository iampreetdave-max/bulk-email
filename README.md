# Cold Email Campaign Tool

A professional, user-friendly web application for managing and executing cold email campaigns at scale. Built with Streamlit, this tool streamlines the process of sending personalized bulk emails with optional PDF attachments.

## 🎯 Features

- **Multi-Provider Support** - Compatible with Gmail, Outlook, Yahoo, and custom SMTP servers
- **Batch Email Sending** - Send to hundreds of recipients from a simple CSV/TXT file
- **PDF Attachments** - Include professional documents with every email
- **Live Progress Tracking** - Real-time status updates and success/failure metrics
- **Email Preview** - See exactly what recipients will receive before sending
- **Rate Limiting** - Configurable delays between sends to avoid spam filters
- **Error Reporting** - Detailed feedback on failed sends with specific error messages
- **Intuitive UI** - No technical knowledge required—guided setup with built-in instructions

## 📋 Requirements

- Python 3.7+
- Streamlit
- Standard library modules (smtplib, email, tempfile)

## 🚀 Quick Start

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cold-email-campaign.git
   cd cold-email-campaign
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the app:**
   Open your browser and navigate to `http://localhost:8501`

### Cloud Deployment (Streamlit Cloud)

1. Push your repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" and connect your GitHub repository
4. Select the branch and `app.py` as the main file
5. Deploy—your app will be live with a public URL!

## 📧 Email Configuration

### Gmail Setup (Recommended)

1. Navigate to [myaccount.google.com](https://myaccount.google.com)
2. Select **Security** from the left menu
3. Enable **2-Step Verification** (if not already enabled)
4. Search for **App passwords** in the settings
5. Select "Mail" and "Windows Computer"
6. Google will generate a 16-character password
7. Copy and paste this password into the app

**Note:** Gmail requires app-specific passwords for security reasons. Your regular Gmail password will not work.

### Outlook Setup

1. Sign in to your Microsoft account
2. Go to [account.microsoft.com/security](https://account.microsoft.com/security)
3. Under "App passwords," create a new password for "Other (Windows, Mac, etc.)"
4. Use this password in the application

### Yahoo Setup

1. Go to [account.yahoo.com](https://account.yahoo.com)
2. Click **Account security**
3. Generate an **App password** for Yahoo Mail
4. Use the generated password in the application

### Custom SMTP

Select "Other" and enter your SMTP server details:
- **Server:** Your SMTP server address (e.g., `mail.customdomain.com`)
- **Port:** Typically 587 (TLS) or 465 (SSL)

## 📁 Email List Format

Your email file can be in either format:

**Comma-separated (single line):**
```
john@company.com, sarah@company.com, mike@company.com
```

**Line-separated (multiple lines):**
```
john@company.com
sarah@company.com
mike@company.com
```

The application automatically detects and parses both formats.

## 🎨 Usage Workflow

1. **Configure Email Account:**
   - Select your email provider
   - Enter your email address and app password

2. **Set Campaign Details:**
   - Enter subject line
   - Set delay between emails (0-10 seconds recommended)

3. **Write Email Content:**
   - Compose your email message in the text area
   - Preview how it will appear to recipients

4. **Upload Files:**
   - Upload your email list (CSV or TXT)
   - Optionally upload a PDF attachment

5. **Review & Send:**
   - Verify all details are correct
   - Click "Send Campaign"
   - Monitor real-time progress and results

## 📊 Results & Reporting

After sending, the application displays:
- **Successful sends** - Number of emails delivered
- **Failed sends** - Number of delivery failures
- **Total sent** - Overall campaign statistics
- **Error details** - Specific issues for troubleshooting

## ⚠️ Best Practices

- **Start small:** Test with a small batch (5-10 emails) first
- **Use delays:** Set 1-2 second delays to avoid triggering spam filters
- **Professional content:** Personalize messages when possible for better engagement
- **Warm-up accounts:** New accounts may have sending limits—gradually increase volume
- **Follow laws:** Comply with CAN-SPAM, GDPR, and other email regulations
- **Monitor deliverability:** Check recipient responses and adjust messaging accordingly

## 🔒 Security & Privacy

- Passwords are **never stored** or logged
- All data is processed in-memory during the session
- PDF files are temporarily stored and automatically deleted after sending
- No data is sent to external servers beyond your email provider
- Use environment variables for sensitive credentials when deploying

## 🐛 Troubleshooting

### "Login failed" Error
- Verify you're using the correct **app password** (not your regular password)
- For Gmail, ensure 2-Step Verification is enabled
- Check that your email provider supports SMTP access

### "Invalid email" Warnings
- Ensure your email list contains valid email addresses with "@" symbol
- Remove extra spaces or special characters from the email list

### Emails Not Sending
- Check your internet connection
- Verify firewall/antivirus isn't blocking SMTP ports (587 or 465)
- Ensure you're not exceeding your email provider's sending limits

### PDF Not Attaching
- Confirm the PDF file is not corrupted and under 25MB
- Verify file permissions allow reading

## 📝 License

This project is licensed under the MIT License—feel free to use, modify, and distribute.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug reports and feature suggestions.

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the maintainer.

---

**Built By Preet Dave**
