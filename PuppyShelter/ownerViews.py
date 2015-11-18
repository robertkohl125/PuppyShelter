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
	if request.method == "POST":
		new_owner = {'name': request.form['name'],
			'needs': request.form['needs'],
			'address': request.form['address'],
			'city': request.form['city'],
			'state': request.form['state'],
			'zipCode': request.form['zipCode']}
		models.createOwner(new_owner)
		return redirect(url_for('owners'))
	else:
		return render_template('ownerNew.html')


#
@app.route('/owners/<int:owner_id>/ownerview', methods = ['GET','POST'])
def ownerView(puppy_id):
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
