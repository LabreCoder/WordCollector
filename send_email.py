#PSEUDO CÓDIGO

'''
Docstring for send_email

Criar a função que irá realizar os envios do e-mail

import smtplib
import email.message

sender_email = 'email@gmail.com'
sender_password = 'senha123'
reseiver_email = 'email@gmail.com'
subject = 'Assunto do e-mail'
body = 'Corpo do e-mail'

def send_email(sender_email, sender_password, receiver_email, subject, body):
    msg = email.message.EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

Depois de criar o e-mail, registrar o que foi enviado no banco de dados. Para isso, criar um código que faça a conexão com o banco de dados e registre as informações do e-mail enviado.

        print('E-mail enviado com sucesso!')
        
'''

