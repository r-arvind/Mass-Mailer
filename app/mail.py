import sendgrid
import os
from sendgrid.helpers.mail import *
def mail(toemail,subject,body):
    sg = sendgrid.SendGridAPIClient(apikey='****API KEY*****')
    list_email = toemail.split(',')
    sender = Email("UMailer@gmail.com")
    content = Content("text/plain", body)
    for i in list_email:
        mail = Mail(sender, subject ,Email(i),content )
        response = sg.client.mail.send.post(request_body=mail.get())
    print "Success"
