from flask import Flask
import flask
app = Flask(__name__)
print flask.__version__

import PuppyShelter.views
import PuppyShelter.models