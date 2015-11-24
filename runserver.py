from PuppyShelter import app
import config
import logging


logging.basicConfig(filename='pslog.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.info('Started server')
app.run(host='0.0.0.0', port=8080)