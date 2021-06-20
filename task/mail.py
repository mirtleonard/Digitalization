from django.core import mail

def sendMail(title, body, to):
    connection = mail.get_connection()
    connection.open()
    email = mail.EmailMessage(
        title,
        body,
        'mirtgiany@yahoo.com',
        to)
    email.send()
    connection.close()
