from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/owners/')
def owners():
    owners = models.selectAllOwners()
    return render_template('ownerAll.html', owners = owners)


#
@app.route('/owners/<int:owner_id>/ownerview/')
def ownerView(owner_id):
	owner = models.selectAllOwners().filter_by(owner_id=owner_id)
	return render_template('ownerView.html', owner = owner, owner_id = owner_id)

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
@app.route('/owners/<int:owner_id>/owneredit', methods = ['GET','POST'])
def ownerEdit(puppy_id):
    return 'owneredit'


#
@app.route('/owner/<int:owner_id>/ownerdelete', methods = ['GET','POST'])
def ownerDelete(owner_id):
	owner = models.selectAllOwners().filter_by(owner_id=owner_id)
	if request.method == "POST":
		models.deleteOwner(owner_id)
		return redirect(url_for('owners'))
	else:
		return render_template('ownerDelete.html', owner = owner, owner_id = owner_id)