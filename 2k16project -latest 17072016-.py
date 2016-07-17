import pymysql, imaplib, re, sys, glob, poplib, smtplib, os, string, time, random
import email, gmail

# import getpass
# getpass.getuser()

# Set default encoding for Python to UTF-8
import codecs
from email.parser import HeaderParser

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from string import Template
from datetime import datetime


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

# Retrieve information from database with Python #
conn = pymysql.connect(host = "localhost",    # host
                     user = "root",         # username
                     passwd = "1234",  		# password
                     db = "fyp_database")        	# name of the database

cur = conn.cursor() # Create a Cursor object, will allow execute all the queries you need

cur.execute("SELECT * FROM fyp") # Use all the SQL

for row in cur.fetchall():
	print(row)


print("*" * 50)

# Inbox #
# Mail status (read, unread, retrieve) and count messages #
def mail():
	while True : 
		# Login to INBOX
		userName = "fyp20166@gmail.com"
		password = "Orange123"
		email_ids = [userName]
		data = []
		imap_server = imaplib.IMAP4_SSL("imap.gmail.com")
		imap_server.login(userName, password)
		imap_server.select('INBOX')
	
	
		# Get count of unseen emails
		(status, response) = imap_server.search(None, '(UNSEEN)')
		unread_msg_nums = response[0].split()
		# Print the count of all unread messages
		print "Number of Unseen Emails : " + str(len(unread_msg_nums))
		print("*" * 50)
	
	
		# To get sender email // use email.message_from_string
		print "Latest email addresses : "
		print(" ")
		email_list = []
		email_unique = []

		result, data = imap_server.search(None, 'UNSEEN')
		ids = data[0]
		id_list = ids.split()
		for i in id_list:
			typ, data = imap_server.fetch(i,'(RFC822)')
			for response_part in data:
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1])
					sender = msg['from'].split()[-1]
					address = re.sub(r'[<>]','',sender)
					# Ignore any occurences of own email address & add to list
					if not re.search(r'' + re.escape(userName),address) and not address in email_list:
						email_list.append(address)
						print address
						print("*" * 50)

			# store output
			# Check if user already exist in DB
			query = "SELECT email FROM fyp WHERE email LIKE address"
			cur.execute(query)
			# data = cur.fetchall()
			options = list(cur.fetchall())
			for i,row in enumerate(cursor.fetchall()):
				options.append(row[i])
				if not options:
					print 'User not found'
				else:
					print 'User found'
						
		
		# # If Unsubscribe
		# if header == "Un-subscribe" :
			# msg = Message.UserNotification(
			# self.GetMemberAdminEmail(addr), self.GetBouncesEmail(),
			# _('You have unsubscribed from the chat service.'),
			# Utils.wrap(self.goodbye_msg), lang)
			# msg.send(self, verp=mm_cfg.VERP_PERSONALIZED_DELIVERIES)

		# else :
			# # Extract Body, "To:"
			# body = None
			# # Walk through the parts of the email to find the text body.
			# if msg.is_multipart():
				# for part in msg.walk():
					# # If part is multipart, walk through the subparts.
					# if part.is_multipart():
						# for subpart in part.walk():
							# if subpart.get_content_type() == 'text/plain':
								# # Get the subpart payload (i.e the message body)
								# body = subpart.get_payload(decode=True)
								# #charset = subpart.get_charset()

					# # Part isn't multipart, so get the email body
					# elif part.get_content_type() == 'text/plain':
						# body = part.get_payload(decode=True)
						# #charset = part.get_charset()

			# # If this isn't a multi-part message then get the payload (i.e the message body)
			# elif msg.get_content_type() == 'text/plain':
				# body = msg.get_payload(decode=True)
				# # No checking done to match the charset with the correct part.
				# for charset in getcharsets(msg):
					# try:
						# body = body.decode(charset)
					# except UnicodeDecodeError:
						# handleerror("UnicodeDecodeError: encountered.",msg,charset)
					# except AttributeError:
						# handleerror("AttributeError: encountered" ,msg,charset)
			# return body
		
		
		# # Forwarding of email 
		# sender = "%s@%s" % (username, imaphost)
		# for num in numbers:
			# resp, data = imap_server.fetch(num, "(RFC822)")
			# text = data[0][1]
			# if options.prefix:
				# parser = email.parser.HeaderParser()
				# msg = parser.parsestr(text)
				# msg['Subject'] = options.prefix + msg['Subject']
				# text = msg.as_string()
			# smtp_server.sendmail(sender, destination, text)
			# # Flag message as Seen (may have already been done by the server anyway)
			# imap_server.store(num, '+FLAGS', '\\Seen')
			
			
# # Mark them as seen
# for e_id in unread_msg_nums:
	# imap.store(e_id, '+FLAGS', '\Seen')
	
# #Update db
# db = pymysql.connect("localhost", "root", "1234", "fyp_database" )
# cursor = db.cursor()

# # SQL query to UPDATE
# sql = "INSERT INTO `fyp_database` (`group`, `email`, `subscription`, `count`, `nickname`) VALUES (%s, %s)"

# try:
	# cursor.execute(sql)
	# # Commit your changes in the database
	# db.commit()
# except:
	# # Rollback in case there is any error
	# db.rollback()

	
# # disconnect from server
# db.close()

# mail.logout()
		break
mail()
cur.close()

conn.close() # Disconnect from server