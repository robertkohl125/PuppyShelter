from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/owners/')
def owners():
    owners = models.selectAllOwners()
    return render_template('ownerAll.html', owners = owners)


#
@app.route('/owners/ownernew', methods = ['GET','POST'])
def ownerNew():
    return 'ownernew'


#
@app.route('/owners/<int:owner_id>/owneredit', methods = ['GET','POST'])
def ownerEdit(puppy_id):
    return 'owneredit'


#
@app.route('/owners/<int:owner_id>/owneradopt', methods = ['GET','POST'])
def ownerAdopt(puppy_id):
    return 'owneradopt'


#
@app.route('/owner/<int:owner_id>/ownerdelete', methods = ['GET','POST'])
def ownerDelete(puppy_id):
    return 'ownerdelete'
