from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email import encoders
# from email.mime.base import MIMEBase

import smtplib, gmail, pymysql, glob, imaplib, os, sys, random

conn = pymysql.connect(host = "localhost", user = "root", passwd = "", db = "mysql")
cur = db.cursor()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

gmail_user = "fyp20166@gmail.com"
gmail_pwd = "Orange123"
server.login(gmail_user, gmail_pwd)

# Create MIME message #
#Send welcome message
strSQL = "SELECT email FROM fyp WHERE subscription = 1"
conn.execute(strSQL)
data = cur.fetchall()
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = strSQL
msg['Subject'] = "Welcome Email"
body = "Thank you for playing!"
msg.attach(MIMEText(body, 'plain'))

try:
	s = smtplib.SMTP("smtp.gmail.com", 587)
	s.starttls()
	s.sendmail(gmail_user, strSQL, msg.as_string())
	print "Successfully sent the mail! :)"
except:
	print "Failed to send mail :("