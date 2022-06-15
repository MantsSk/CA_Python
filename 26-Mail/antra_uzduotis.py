import smtplib
from email.message import EmailMessage
from string import Template
import os

def apmokek(kreipinys, elpastas, suma):
    
    with open('skola.html', 'r') as f:
        html = f.read()

    sablonas = Template(html)
    
    email = EmailMessage()
    email['from'] = 'Skolos administratorius'
    email['to'] = 'testmailcodeacademy@gmail.com'
    email['subject'] = 'Pranešimas apie įsiskolinimą'

    email.set_content(sablonas.substitute(
        {'kreipinys': kreipinys, 
        'skola': suma, 
        'mail': elpastas}), 
        'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('testmailcodeacademy@gmail.com', os.environ["MAIL_PASSWORD"])
        smtp.send_message(email)

apmokek('Antanai', 'adresatas@gmail.com', 25.25)