import requests
from time import sleep
import smtplib
from email.message import EmailMessage
from string import Template
import os

def send_mail(error):
    message = '''
    Dėmesio!

    Pranešame, kad negautas atsakas iš jūsų serverio. Klaidos žinutė tokia:

    $error
    '''
    sablonas = Template(message)

    email = EmailMessage()
    email['from'] = 'Vardas Pavardė'
    email['to'] = 'testmailcodeacademy@gmail.com'
    email['subject'] = 'email from python'

    email.set_content(sablonas.substitute({'error': e}), 'plain')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('testmailcodeacademy@gmail.com', os.environ["MAIL_PASSWORD"])
        smtp.send_message(email)


while True:
    try:
        res = requests.get('http://127.0.0.1:8000')
        print(res.status_code)
        sleep(5)
    except requests.ConnectionError as e:
        print(e)
        send_mail(e)
        break