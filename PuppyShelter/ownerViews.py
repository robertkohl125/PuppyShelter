from PuppyShelter import app, models, forms
from flask import render_template, url_for, request, redirect, flash, jsonify
import logging 


logging.info('ownerViews.py file accessed ')


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
	a = puppy.scalar()
	if a is None:
		pups = "No puppies adopted yet!"
	else:
		pups = "Adopted Puppies:"
	print pups
	return render_template('ownerView.html', 
		owner_id = owner_id, 
		owner = owner, 
		puppy = puppy, 
		pups = pups)

#
@app.route('/owners/ownernew', methods = ['GET','POST'])
def ownerNew():
	form = forms.OwnerForm(request.form)
	if request.method == "POST" and form.validate():
		new_owner = {
			'firstName': form.firstName.data,
			'lastName': form.lastName.data,
			'address': form.address.data,
			'city': form.city.data,
			'state': form.state.data,
			'zipCode': form.zipCode.data,
			'email': form.email.data,
			'needs': form.needs.data}
		models.createOwner(new_owner)
		flash('A new owner is ready to adopt!')
		return redirect(url_for('owners'))
	else:
		return render_template('ownerNew.html', form = form)


#
@app.route('/owners/<int:owner_id>/owneredit', methods = ['GET','POST'])
def ownerEdit(owner_id):
	owner = models.selectAllOwners().filter_by(owner_id=owner_id)
	if request.method == "POST":
		edit_owner = {
			'firstName': request.form['firstName'],
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

app.secret_key = 'super_secret_key'