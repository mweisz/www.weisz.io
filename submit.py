#!/usr/bin/python3.6

import cgi
import smtplib

import cgitb
cgitb.enable()

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

parameters = cgi.FieldStorage()
try:
    # Parse Parameters
    first_name = parameters['first_name'].value
    last_name = parameters['last_name'].value
    email = parameters['email'].value
    comment = parameters['comment'].value


    frm = "no-reply@weisz.io"
    to = "mail@michael-weisz.de"
    body = """First Name: {} <br>
Last Name: {} <br>
Email: {} <br>
Message: {}""".format(first_name, last_name, email, comment)

    # Assemble Message
    msg = MIMEMultipart('alternative')
    msg.set_charset('utf8')
    
    msg['FROM'] = frm
    msg['Subject'] = 'Message via weisz.io contact form'
    msg['To'] = to

    _attach = MIMEText(body.encode('utf-8'), 'html', 'UTF-8')        
    msg.attach(_attach)

    server = smtplib.SMTP('localhost')
    server.sendmail(frm, to, msg.as_string())
    server.quit()

    print('Status: 200 OK')
    print("Content-type:text/html\r\n\r\n")

except KeyError:
    print('Status: 400 Bad Request')
    exit(1)
except smtplib.SMTPException:
    print('Status: 520 Bad Request')
    exit(1)