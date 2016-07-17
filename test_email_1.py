from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import cgi, glob, pymysql, imaplib, smtplib, os, gmail, sys, random

server = smtplib.SMTP('smtp.gmail.com', 587)
# Set up connection for sending mail #
server.ehlo()
server.starttls()
server.ehlo()

data = None
form = cgi.FieldStorage()

first_names = {"jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul", "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren", "ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet", "lydia", "charles", "pedro", "bradley"}
last_names = {"barker", "style", "spirits", "murphy", "blacker", "bleacher", "rogers", "warren", "keller"}

def Name(first_names, last_names):
	first = random.sample(first_names, 1)[0]
	last = random.sample(last_names - {first}, 1)[0]
	return (first + " " + last)

OUT=[]

i=100
while i > 0:
    name=Name(first_names, last_names)
    if name not in OUT:
        OUT.append(name)
        print name
    i-=1

print len(OUT), 'unique names generated.'

def dataBase1(host, user, passwd, db):
    db = pymysql.connect(host="localhost", user="root", passwd=" ", db="c207")
    cursor = db.cursor()
    cursor.execute(cmd)
    global data
    data = cursor.fetchone()
    db.close()

def sendMail(fromaddr, toaddr, subject, msg, gmail_user, gmail_password, smtpserver = 'smtp.gmail.com:587'):
	gmail_user = 'fyp20166@gmail.com'  
	gmail_password = 'Orange123'
	
	# Create MIME message #
	#Send (welcome) message
	msg = MIMEMultipart()
	msg = MIMEText("""body""")
	sender = 'fyp20166@gmail.com'
	recipients = ['velvetkxtten@gmail.com']
	msg['Subject'] = "Welcome"
	msg['From'] = sender
	msg['To'] = ", ".join(recipients)
	s.sendmail(sender, recipients, msg.as_string())
	
	#Attach body of email to MIME message
	body = "Welcome to our chat service! \r\nThank you for choosing us!"
	msg.attach(MIMEText(body, 'plain'))

	#Unsubscribe email
	mailSend = True
	while mailSend:
	
		try:  
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # Insert GMail SMTP server domain name
			server.ehlo() #Saying "hello" to the SMTP server
			server.login(gmail_user, gmail_password)
			server.close()
			print 'Yay, email sent! :)'
		except:  
			print 'Something went wrong :('

# print "Content-Type: text/html"
# print ""
# print "<html>"
# print "<h2>CGI Script Output</h2>"
# print "</p>"
# print "</html>"