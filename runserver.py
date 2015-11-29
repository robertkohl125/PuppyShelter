from PuppyShelter import app
#import logging


app.config['DEBUG'] = True
#logging.info('runserver.py file accessed ')
app.run(host='0.0.0.0', port=8080)
