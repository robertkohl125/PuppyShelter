from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/puppies/')
def puppies():
    puppies = models.selectAllPuppies()
    return render_template('puppyAll.html', puppies = puppies)


#
@app.route('/puppies/puppynew', methods = ['GET','POST'])
def puppyNew():
    return 'puppynew'


#
@app.route('/puppies/<int:puppy_id>/puppyedit', methods = ['GET','POST'])
def puppyEdit(puppy_id):
    return 'puppyedit'



@app.route('/puppies/<int:puppy_id>/puppyview', methods = ['GET','POST'])
def puppyView(puppy_id):
    return 'puppyedit'
#
#@app.route('/puppies/<int:puppy_id>/puppyadopt', methods = ['GET','POST'])
#def puppyAdopt(puppy_id):
#    return 'puppyadopt'


#
@app.route('/puppies/<int:puppy_id>/puppydelete', methods = ['GET','POST'])
def puppyDelete(puppy_id):
    return 'puppydelete'


