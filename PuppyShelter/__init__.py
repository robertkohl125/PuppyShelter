from flask import Flask
import sys
import flask
import logging
import logging.handlers


#logging.shutdown()

logging.basicConfig(
	filename='logs/MainLog.log')
f = logging.Formatter(
	fmt='%(levelname)s:%(name)s: %(filename)s: %(message)s '
	'(%(asctime)s; %(lineno)d)',
    datefmt="%Y-%m-%d %H:%M:%S")
handlers = [
    logging.handlers.RotatingFileHandler(
    	'logs/MainLog-old.log', 
    	encoding='utf8',
        maxBytes=10000, 
        backupCount=5),
    logging.StreamHandler()]

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
for h in handlers:
    h.setFormatter(f)
    h.setLevel(logging.DEBUG)
    root_logger.addHandler(h)

logging.info('__init__.py file accessed ')

app = Flask(__name__)


print "Flask version", flask.__version__
print "Python version", (sys.version)


import PuppyShelter.mainView
import PuppyShelter.ownerViews
import PuppyShelter.puppyViews
import PuppyShelter.shelterViews
import PuppyShelter.models
import PuppyShelter.forms
import sms


