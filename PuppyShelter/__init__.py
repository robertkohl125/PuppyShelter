from flask import Flask
import flask
app = Flask(__name__)
print flask.__version__

import PuppyShelter.mainView
import PuppyShelter.ownerViews
import PuppyShelter.puppyViews
import PuppyShelter.shelterViews
import PuppyShelter.models
import PuppyShelter.forms