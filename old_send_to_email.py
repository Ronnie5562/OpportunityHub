import smtplib
from email.message import EmailMessage
from os import getenv


EMAIL_ADDRESS = getenv("EMAIL_USER")
EMAIL_PASSWORD = getenv("EMAIL_PASS")


def send_email(email, job_list, job_type):
    message = EmailMessage()
    message['Subject'] = f"{job_type} Jobs For You !!!"
    message['From'] = EMAIL_ADDRESS
    message['To'] = email
    message.set_content('This is a plain text')

    job_listings = ""
    for job in job_list:
        job_listings += f"""\n
        <div class="job-listing">
            <h2>Job Title: {job['job_title']}</h2>
            <p>Company: {job['company_name']}</p>
            <p>Location: {job['location']}</p>
            <p>Description: {job['summary']}</p>
            <a href="{job['url']}" target="_blank">Learn More</a>
        </div>
        """

    styles = '''
    <style>
        body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        }
        .header {
        background-color: #3498db;
        color: white;
        text-align: center;
        padding: 1em;
        }
        .job-listing {
        border: 1px solid #ddd;
        padding: 1em;
        margin: 1em;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .footer {
        background-color: #f9f9f9;
        text-align: center;
        padding: 1em;
        }
    </style>
    '''

    content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    {styles}
    
    </head>
    <body>
    <div class="header">
        <h1>OpportunityHUB Job Opportunities</h1>
        <p>Your source for the latest job opportunities!</p>
    </div>
    
    {job_listings}
    
    <div class="footer">
        <p>For more job opportunities and information, visit <a href="https://www.opportunityhub.com" target="_blank">OpportunityHUB</a>.</p>
        <p>Contact us at <a href="mailto:info@opportunityhub.com">info@opportunityhub.com</a>.</p>
        <p>Copyright © 2023, OpportunityHub, Inc.</p>
    </div>
    </body>
    </html>    
    '''

    message.add_alternative(content, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(message)


if __name__ == "__main__":
    email = input('Enter your email: ')

    send_email(email)
