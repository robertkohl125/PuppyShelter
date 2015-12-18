from flask.ext.mail import Mail, Message
import logging 
from flask import Flask
app = Flask(__name__)


mail = Mail(app)
mail.DEFAULT_MAIL_SENDER = "senderemail@emai.com" #enter default sender email address.

def email(text, recipient):
	text1 = "Thank you for visiting us today! This email is to confirm "
	print 'Email To:',recipient
	print text1, text
#	msg = Message(text1 + text,
#		recipients = [recipients])
#	mail.send(msg)
#	logging.info("**email sent to %s." % (recipient))