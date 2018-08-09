import smtplib

def send_registration_email():
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    gmail_pass = 'EnterGmailPassHere'
    server.login('amirmahdi76@gmail.com',gmail_pass)

    sender = 'amirmahdi76@gmail.com'
    reciever = 'amirmahdi76@gmail.com'
    msge = '\nhttps://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=ECON&course=102&section=008'

    server.sendmail(sender,reciever,msge)