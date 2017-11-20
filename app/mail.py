import sendgrid
import os
from sendgrid.helpers.mail import *
def mail(toemail,subject,body):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    list_email = toemail.split(',')
    sender = Email("UMailer@gmail.com")
    content = Content("text/plain", body)
    for i in list_email:
        mail = Mail(sender, subject ,Email(i),content )
        response = sg.client.mail.send.post(request_body=mail.get())
    print "Success"
