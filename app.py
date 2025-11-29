import streamlit as st
import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import tempfile

st.set_page_config(page_title="Cold Email Campaign", layout="wide")

st.title("🚀 Cold Email Campaign Tool")

# Sidebar for setup instructions
with st.sidebar:
    st.header("Setup Instructions")
    st.markdown("""
    ### Gmail Setup
    1. Go to [myaccount.google.com](https://myaccount.google.com)
    2. Click **Security** on the left
    3. Enable **2-Step Verification** if not already on
    4. Search for **App passwords**
    5. Select Mail and Windows Computer
    6. Copy the generated 16-character password
    7. Use it in this app
    
    ### Other Email Providers
    - **Outlook**: Use your password directly
    - **Yahoo**: Generate App password in Account Security
    """)

# Main content
col1, col2 = st.columns(2)

with col1:
    st.header("📧 Email Configuration")
    
    email_provider = st.selectbox("Email Provider", ["Gmail", "Outlook", "Yahoo", "Other"])
    sender_email = st.text_input("Your Email Address")
    sender_password = st.text_input("App Password/Password", type="password")
    
    # SMTP settings based on provider
    smtp_settings = {
        "Gmail": {"server": "smtp.gmail.com", "port": 587},
        "Outlook": {"server": "smtp-mail.outlook.com", "port": 587},
        "Yahoo": {"server": "smtp.mail.yahoo.com", "port": 587},
        "Other": {"server": st.text_input("SMTP Server"), "port": st.number_input("SMTP Port", value=587)}
    }
    
    current_settings = smtp_settings[email_provider]

with col2:
    st.header("📋 Campaign Details")
    
    subject = st.text_input("Email Subject")
    delay_seconds = st.slider("Delay between emails (seconds)", 0, 10, 1)

st.divider()

st.header("📨 Email Content")
email_body = st.text_area("Email Body", height=200, placeholder="Type your email message here...")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("📥 Upload Files")
    
    email_file = st.file_uploader("Upload email list (.txt or .csv)", type=["txt", "csv"])
    pdf_file = st.file_uploader("Upload PDF attachment (optional)", type=["pdf"])

with col2:
    st.header("👁️ Preview")
    
    if email_body:
        st.markdown("**Email Preview:**")
        st.markdown(f"**Subject:** {subject}")
        st.text_area("Body Preview:", value=email_body, height=150, disabled=True)
        
        if pdf_file:
            st.success(f"✓ PDF attached: {pdf_file.name}")

st.divider()

def parse_emails(file_content):
    """Parse emails from file content"""
    text = file_content.decode('utf-8')
    
    # Try comma-separated first
    if ',' in text:
        emails = [email.strip() for email in text.split(',')]
    else:
        emails = [email.strip() for email in text.split('\n')]
    
    # Filter out empty strings and validate basic email format
    emails = [email for email in emails if email and '@' in email]
    return emails

def send_emails(sender_email, sender_password, smtp_server, smtp_port, subject, body, email_list, pdf_path=None):
    """Send emails to multiple recipients"""
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    results = {"successful": 0, "failed": 0, "errors": []}
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        for index, recipient in enumerate(email_list):
            try:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient
                msg['Subject'] = subject
                
                msg.attach(MIMEText(body, 'plain'))
                
                # Attach PDF if provided
                if pdf_path:
                    with open(pdf_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    
                    encoders.encode_base64(part)
                    filename = os.path.basename(pdf_path)
                    part.add_header('Content-Disposition', 'attachment', filename=filename)
                    msg.attach(part)
                
                server.send_message(msg)
                results["successful"] += 1
                status_text.info(f"✓ Sent to {recipient} ({index + 1}/{len(email_list)})")
                
            except Exception as e:
                results["failed"] += 1
                results["errors"].append(f"{recipient}: {str(e)}")
                status_text.warning(f"✗ Failed to send to {recipient}")
            
            # Update progress
            progress_bar.progress((index + 1) / len(email_list))
            
            # Delay between emails
            if index < len(email_list) - 1:
                time.sleep(delay_seconds)
        
        server.quit()
        return results
    
    except Exception as e:
        st.error(f"Connection Error: {str(e)}")
        return None

# Send button
if st.button("🚀 Send Campaign", type="primary", use_container_width=True):
    
    # Validation
    if not sender_email or not sender_password:
        st.error("❌ Please enter your email and password")
    elif not subject or not email_body:
        st.error("❌ Please enter subject and email body")
    elif not email_file:
        st.error("❌ Please upload an email list file")
    else:
        # Parse emails
        emails = parse_emails(email_file.read())
        
        if not emails:
            st.error("❌ No valid emails found in file")
        else:
            st.success(f"✅ Found {len(emails)} emails")
            
            # Handle PDF
            pdf_path = None
            if pdf_file:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(pdf_file.read())
                    pdf_path = tmp.name
            
            # Send emails
            st.header("📤 Sending Emails...")
            results = send_emails(
                sender_email,
                sender_password,
                current_settings["server"],
                current_settings["port"],
                subject,
                email_body,
                emails,
                pdf_path
            )
            
            if results:
                st.divider()
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Successful", results["successful"])
                with col2:
                    st.metric("Failed", results["failed"])
                with col3:
                    st.metric("Total", len(emails))
                
                if results["errors"]:
                    st.error("**Errors encountered:**")
                    for error in results["errors"]:
                        st.text(error)
                else:
                    st.success("✅ All emails sent successfully!")
            
            # Cleanup
            if pdf_path and os.path.exists(pdf_path):
                os.remove(pdf_path)
