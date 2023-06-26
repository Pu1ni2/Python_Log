import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# Server configuration
SMTP_SERVER = 'your_smtp_server'
SMTP_PORT = 587
SMTP_USERNAME = 'your_username'
SMTP_PASSWORD = 'your_password'
SENDER_EMAIL = 'sender@example.com'
RECIPIENT_EMAIL = 'recipient@example.com'

def export_running_jobs():
    # Get list of running processes
    running_jobs = []
    for proc in psutil.process_iter(['pid', 'name']):
        running_jobs.append((proc.info['pid'], proc.info['name']))
    
    # Export running jobs to a file
    with open('running_jobs.txt', 'w') as file:
        for pid, name in running_jobs:
            file.write(f'PID: {pid}\tName: {name}\n')

    # Send email with the exported file as an attachment
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = 'Running Jobs Report'

    body = 'Please find attached the list of running jobs.'
    msg.attach(MIMEText(body, 'plain'))

    with open('running_jobs.txt', 'rb') as attachment:
        part = MIMEText(attachment.read(), 'plain')
        part.add_header('Content-Disposition', 'attachment', filename='running_jobs.txt')
        msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

    print('Running jobs exported and email sent successfully.')

# Schedule the export and email task to run every hour
schedule.every().hour.do(export_running_jobs)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
