import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'first_name last_name'
email['to'] = 'testbyrandom@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    print(email)
    smtp.login('testrandom@gmail.com', 'testpassword')
    smtp.send_message(email)
    print('all good boss!')
