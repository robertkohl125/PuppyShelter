from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify
#app.run(debug=True)

@app.route('/')
def index():
   return 'hello'


@app.route('/shelters')
def shelters():
    shelters = models.showShelter()
    print shelters
    return render_template('shelterAll.html', shelters = shelters)


#
@app.route('/shelters/shelterview', methods = ['GET','POST'])
def shelterView():
    return 'shelterview'


#
@app.route('/shelters/shelternew', methods = ['GET','POST'])
def shelterNew():
    return 'shelternew'


#
@app.route('/shelters/<int:shelter_id>/shelteredit', methods = ['GET','POST'])
def shelterEdit(shelter_id):
    return 'shelteredit'


#
@app.route('/shelters/<int:shelter_id>/shelterdelete', methods = ['GET','POST'])
def shelterDelete(shelter_id):
    return 'shelterdelete'


#
@app.route('/puppy/')
def puppy():
    return 'puppy'


#
@app.route('/puppy/puppynew', methods = ['GET','POST'])
def puppyNew():
    return 'puppynew'


#
@app.route('/pyppy/<int:puppy_id>/puppyedit', methods = ['GET','POST'])
def puppyEdit(puppy_id):
    return 'puppyedit'


#
@app.route('/pyppy/<int:puppy_id>/puppyadopt', methods = ['GET','POST'])
def puppyAdopt(puppy_id):
    return 'puppyadopt'


#
@app.route('/pyppy/<int:puppy_id>/puppydelete', methods = ['GET','POST'])
def puppyDelete(puppy_id):
    return 'puppydelete'

