import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def create_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Create the MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    with open(attachment_path, 'rb') as attachment:
        # Create a MIMEBase object
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    # Encode the file in base64
    encoders.encode_base64(part)

    # Add header to the attachment
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')

    # Attach the file to the message
    msg.attach(part)

    # Connect to the Gmail server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your email account
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)

    # Quit the server
    server.quit()

# Example usage
if __name__ == "__main__":
    # File creation
    file_path = "example.txt"
    content = "This is a sample file content."
    create_file(file_path, content)

    # Email sending
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    receiver_email = "receiver_email@example.com"
    subject = "Subject of the Email"
    body = "This is the body of the email."

    send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, file_path)

    print(f"Email sent successfully with {file_path} as an attachment.")