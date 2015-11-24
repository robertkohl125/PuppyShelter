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
	puppy = models.selectAllPuppies().filter_by(owner_id=owner_id)
	owner = models.selectAllOwners().filter_by(owner_id=owner_id)
#	puppy = models.selectAllPuppies().filter_by(puppy_id = pup)
	return render_template('ownerView.html', owner_id = owner_id, owner=owner, puppy = puppy)

#
@app.route('/owners/ownernew', methods = ['GET','POST'])
def ownerNew():
#	form = form.OwnerForm(request.form)
	if request.method == "POST":
		new_owner = {'firstName': request.form['firstName'],
			'lastName': request.form['lastName'],
			'address': request.form['address'],
			'city': request.form['city'],
			'state': request.form['state'],
			'zipCode': request.form['zipCode'],
			'email': request.form['email'],
			'needs': request.form['needs']}
		models.createOwner(new_owner)
		return redirect(url_for('owners'))
	else:
		return render_template('ownerNew.html')


#
@app.route('/owners/<int:owner_id>/owneredit', methods = ['GET','POST'])
def ownerEdit(owner_id):
	owner = models.selectAllOwners().filter_by(owner_id=owner_id)
	if request.method == "POST":
		edit_owner = {'firstName': request.form['firstName'],
			'lastName': request.form['lastName'],
			'address': request.form['address'],
			'city': request.form['city'],
			'state': request.form['state'],
			'zipCode': request.form['zipCode'],
			'email': request.form['email'],
			'needs': request.form['needs']}
		models.editOwner(edit_owner, owner_id)
		return redirect(url_for('owners'))
	else:
		return render_template('ownerEdit.html', owner = owner)


#
@app.route('/owner/<int:owner_id>/ownerdelete', methods = ['GET','POST'])
def ownerDelete(owner_id):
	owner = models.selectAllOwners().filter_by(owner_id=owner_id)
	if request.method == "POST":
		models.deleteOwner(owner_id)
		return redirect(url_for('owners'))
	else:
		return render_template('ownerDelete.html', owner = owner, owner_id = owner_id)