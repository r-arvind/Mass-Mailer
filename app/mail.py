import sendgrid
import os
from sendgrid.helpers.mail import *
def mail(toemail,subject,body):
<<<<<<< HEAD
    sg = sendgrid.SendGridAPIClient(apikey= '*****************APIKEY********************')
=======
    sg = sendgrid.SendGridAPIClient(apikey='****API KEY*****')
>>>>>>> d7806d2c3c1cb955756714b8fa06562068c3e2e1
    list_email = toemail.split(',')
    sender = Email("UMailer@gmail.com")
    content = Content("text/plain", body)
    for i in list_email:
        mail = Mail(sender, subject ,Email(i),content )
        response = sg.client.mail.send.post(request_body=mail.get())
    print "Success"
