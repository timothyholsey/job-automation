import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def read_job_listings(file_path):
    jobs = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            jobs.append(row)
    return jobs

def rank_jobs_by_profitability(jobs):
    # Assuming 'profit_margin' is a key in the job dictionary
    return sorted(jobs, key=lambda x: float(x['profit_margin']), reverse=True)

def generate_outreach_email(job):
    subject = f"Opportunity: {job['title']}"
    body = f"Dear {job['contact_name']},\n\nWe noticed your listing for {job['title']} and believe we can offer great value..."
    return subject, body

def send_email(subject, body, recipient_email):
    sender_email = "your_email@example.com"
    password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)

if __name__ == "__main__":
    jobs = read_job_listings('job_listings.csv')
    ranked_jobs = rank_jobs_by_profitability(jobs)

    for job in ranked_jobs[:10]:  # Top 10 jobs
        subject, body = generate_outreach_email(job)
        send_email(subject, body, job['contact_email'])
