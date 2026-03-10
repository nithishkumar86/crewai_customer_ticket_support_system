import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.Schema.schemas import EmailDraft
import os


def load_environtment():
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

    if not SENDER_EMAIL:
        return "there is not SENDER_EMAIL in the .env file"
    
    if not SENDER_PASSWORD:
        return "there is not SENDER_PASSWORD in the .env file"
    
    if SENDER_EMAIL and SENDER_PASSWORD:
        return SENDER_EMAIL,SENDER_PASSWORD
    

# ─────────────────────────────────────────────
# Callback — Email Drafter Task (Task 4)
# ─────────────────────────────────────────────
def send_email_callback(output):
    SENDER_NAME, SENDER_PASSWORD = load_environtment()
    try:
        email_draft: EmailDraft = output.pydantic

        msg = MIMEMultipart()
        msg["From"] = SENDER_NAME
        msg["To"] = email_draft.sent_to
        msg["Subject"] = email_draft.email_subject
        msg.attach(MIMEText(email_draft.email_body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_NAME, SENDER_PASSWORD)
            server.sendmail(SENDER_NAME, email_draft.sent_to, msg.as_string())

        print(f"✅ Email sent successfully to {email_draft.sent_to}")
        print(f"📧 Subject: {email_draft.email_subject}")

    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")