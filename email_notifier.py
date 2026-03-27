# Email Notifier
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from typing import List

class EmailNotifier:
    """
    Send email notifications for various events
    """
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.password = password
    
    def send_email(self, recipient: str, subject: str, body: str, is_html: bool = False):
        """
        Send a single email
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'html' if is_html else 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.send_message(msg)
            
            print(f"✓ Email sent to {recipient}")
            return True
        except Exception as e:
            print(f"✗ Failed to send email: {e}")
            return False
    
    def send_bulk_emails(self, recipients: List[str], subject: str, body: str):
        """
        Send emails to multiple recipients
        """
        success_count = 0
        for recipient in recipients:
            if self.send_email(recipient, subject, body):
                success_count += 1
        
        print(f"\nEmailer sent {success_count}/{len(recipients)} emails")
        return success_count
    
    def send_alert_notification(self, recipient: str, alert_type: str, message: str, severity: str = "medium"):
        """
        Send an alert notification email
        """
        severity_colors = {
            'low': '#FFA500',
            'medium': '#FF6347',
            'high': '#DC143C'
        }
        
        color = severity_colors.get(severity, '#808080')
        html_body = f"""
        <html>
            <body>
                <h2 style="color: {color};">[{severity.upper()}] {alert_type}</h2>
                <p>{message}</p>
                <hr>
                <p><small>This is an automated alert notification</small></p>
            </body>
        </html>
        """
        
        return self.send_email(recipient, f"Alert: {alert_type}", html_body, is_html=True)

def create_email_config(config_file: str) -> dict:
    """
    Load email configuration from JSON file
    """
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Configuration file '{config_file}' not found")
        return {}

if __name__ == "__main__":
    print("Email Notifier Tool v1.0")
    print("Configure SMTP settings to enable email sending")
