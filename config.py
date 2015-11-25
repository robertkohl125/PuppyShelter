from PuppyShelter import app
import logging

app.config['DEBUG'] = True
app.secret_key = 'super_secret_key'
logging.basicConfig(
	filename='mainlog.log',
	level=logging.DEBUG,
	format='%(asctime)s %(message)s')
logging.info('***Started server***')