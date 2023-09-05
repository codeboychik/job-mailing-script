import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

import dotenv

dotenv.load_dotenv()


def send_email(receiver, subject, details):
    host = 'smtp.gmail.com'
    port = 465

    message = MIMEMultipart()
    message['From'] = os.getenv('EMAIL_FROM')
    message['To'] = receiver
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(details, 'html'))

    password = os.getenv('EMAIL_PASS')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(message['From'], password)
        server.sendmail(message['From'], receiver, message.as_string())


