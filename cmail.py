import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('agsalekhya474@gmail.com','legv mymy dzlb pgja')#legv mymy dzlb pgja
    msg=EmailMessage()
    msg['FROM']='agsalekhya474@gmail.com'
    msg['To']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()