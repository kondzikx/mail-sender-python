#Author: Konrad Gołuński Copyright
#Mail Sender
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

msg = MIMEMultipart()

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

#checking if login and email are correct if not return invalid email or password - try again
while True:
   try: 
      msg['From'] = input('Podaj maila: ')
      password = getpass('Podaj hasło: ')
      server.login(msg['From'], password)
   except smtplib.SMTPAuthenticationError:
      print('Nieprawidłowe dane logowania! Spróbuj ponownie: ')
   else: 
      print('Zalogowano! Witaj {}'.format(msg['From']))
      break


'''creating variables which cointain main arguments in sendmail function,
which are sender, receiver and combined subject and content of the message'''

msg['To'] = input('Do kogo chcesz wysłać wiadomość?: ')
msg['Subject'] = input('Podaj tytuł: ')
content = input('Napisz wiadomość: ')
msg.attach(MIMEText(content, 'plain'))
email = msg.as_string()

#sending function, which takes 3 arguments as higher
server.sendmail(msg['From'], msg['To'], email)
server.quit()

#after-sended message
print('Wysłano wiadomość do {}'.format(msg['To']))