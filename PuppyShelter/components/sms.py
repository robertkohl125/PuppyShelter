from twilio.rest import TwilioRestClient
import logging 


# To find these visit https://www.twilio.com/user/account
account_sid = 'sid'
auth_token = 'token'
client = TwilioRestClient(account_sid, auth_token)
sender = "5555555555"#your phone number


def sms(text,recipient):
	print 'sms To:',recipients
	print '"',text,'"'
	message = client.messages.create(
		body=etext,
		to = recipient, 
		from_ = sender,)
	logging.info('**sms sent to %s.', recipient)