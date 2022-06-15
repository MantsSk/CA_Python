import requests
from time import sleep
import smtplib
from email.message import EmailMessage
import os
from datetime import datetime

def send_mail(file):
    message = '''
    Dėmesio!
    
    Pranešame, kad negautas atsakas iš jūsų serverio. Prisegame log.txt
    '''
        
    email = EmailMessage()
    email['from'] = 'Vardas Pavardė'
    email['to'] = 'testmailcodeacademy@gmail.com'
    email['subject'] = 'email from python'
    
    email.set_content(message)

    with open(file, 'rb') as f:
        content = f.read()
        filename = f.name
        email.add_attachment(
            content, 
            maintype='text/plain', 
            subtype='plain', 
            filename=filename)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('testmailcodeacademy@gmail.com', os.environ["MAIL_PASSWORD"])
        smtp.send_message(email)

while True:
    try:
        res = requests.get('http://127.0.0.1:8000')
        with open('log.txt', 'a') as log:
            log.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {res.status_code} OK\n')
            sleep(5)
    except requests.ConnectionError as e:
        with open('log.txt', 'a') as log:
            log.write(str(e))
        send_mail('log.txt')
        break