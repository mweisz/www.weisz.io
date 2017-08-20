#!/usr/bin/python3.6

import cgi
import smtplib

import cgitb
cgitb.enable()

parameters = cgi.FieldStorage()
try:
    first_name = parameters['first_name'].value
    last_name = parameters['last_name'].value
    email = parameters['email'].value
    comment = parameters['comment'].value
    print("Content-type:text/html\r\n\r\n")
    print(first_name, last_name, email, comment)

    body = """From: Weisz.io Contact Form <no-reply@weisz.io>
To: Michael Weisz <mail@michael-weisz.de>
MIME-Version: 1.0
Content-type: text/html
Subject: Message via weisz.io contact form

First Name: {} <br>
Last Name: {} <br>
Email: {} <br>
Message: {}""".format(first_name, last_name, email, comment)

    server = smtplib.SMTP('localhost')
    server.sendmail('sender@address8912309123.com', 'mail@michael-weisz.de', body)
    server.quit()
except KeyError:
    print('Status: 400 Bad Request')
    exit(1)
except SMTPException:
    print('Status: 500 Bad Request')
    exit(1)



