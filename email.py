from flask import Flask
from flaskext.mail import Mail
import logging 


app = Flask(__name__)
mail = Mail(app)
mail.DEFAULT_MAIL_SENDER = "senderemail@emai.com" #enter default sender email address.

def email(etext, recipients):
	msg = Message(etext,
		recipients = [etext])
	logging.info('**email sent to %s.', recipient)