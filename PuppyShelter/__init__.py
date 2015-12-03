from flask import Flask
import flask
import sys
import logging
import logging.handlers


print "Flask version", flask.__version__
print "Python version", (sys.version)


#To restart logging service use: logging.shutdown()
def log():
#    logging.basicConfig(filename='logs/MainLog.log')
    format = logging.Formatter(
        fmt='%(levelname)s:%(filename)s: %(message)s '
        '(%(asctime)s; %(lineno)d)',
        datefmt="%Y-%m-%d %H:%M:%S")
    handlers = [
        logging.handlers.RotatingFileHandler(
            'logs/MainLog.log', 
            maxBytes=5000, 
            backupCount=5),
        logging.StreamHandler()]
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    for h in handlers:
        h.setFormatter(format)
        h.setLevel(logging.DEBUG)
        root_logger.addHandler(h)
log()


from flask.ext.mail import Mail 

app = Flask(__name__)
import PuppyShelter.mainView
import PuppyShelter.ownerViews
import PuppyShelter.puppyViews
import PuppyShelter.shelterViews
import PuppyShelter.models
import PuppyShelter.forms
import PuppyShelter.sms
import PuppyShelter.email

#logging.info('__init__.py file accessed ')







