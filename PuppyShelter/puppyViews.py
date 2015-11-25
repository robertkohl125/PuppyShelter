from PuppyShelter import app, models, forms
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/puppies/')
def puppies():
	puppies = models.selectAllPuppies()
	return render_template('puppyAll.html', puppies = puppies)


#
@app.route('/puppies/<int:puppy_id>/puppyview/')
def puppyView(puppy_id):
	puppy = models.selectAllPuppies().filter_by(puppy_id = puppy_id)
	owner = models.selectAdopterOwners(puppy_id)
	shelter = models.selectEnrolledShelter(puppy_id)
	a = models.selectAdopterOwners(puppy_id).scalar()
	for p in puppy:
		print p.picture
	if a is None:
		att = 'enabled'
	else:
		att = 'disabled'
	return render_template('puppyView.html', 
		puppy = puppy, puppy_id = puppy_id, shelter = shelter, owner = owner, att = att)


#
@app.route('/puppies/puppynew', methods = ['GET','POST'])
def puppyNew():
	form = form.PuppyForm(request.form)
	shelters = models.selectAvailableShelters()
	if request.method == "POST":
		new_puppy = {'name': request.form['name'],
			'gender': request.form['gender'],
			'dateOfbirth': request.form['dateOfbirth'],
			'picture': request.form['picture'],
			'breed': request.form['breed'],
			'weight': request.form['weight'],
			'shelter_id': request.form['shelter_id']}
		models.createPuppy(new_puppy)
		return redirect(url_for('puppies'))
	else:
		return render_template('puppyNew.html', shelters = shelters, form = form)


#
@app.route('/puppies/<int:puppy_id>/puppyedit', methods = ['GET','POST'])
def puppyEdit(puppy_id):
	puppy = models.selectAllPuppies().filter_by(puppy_id=puppy_id)
	shelter = models.selectEnrolledShelter(puppy_id)
	shelters = models.selectAvailableShelters()
	if request.method == "POST":
		edit_puppy = {'name': request.form['name'],
			'gender': request.form['gender'],
			'dateOfbirth': request.form['dateOfbirth'],
			'picture': request.form['picture'],
			'breed': request.form['breed'],
			'weight': request.form['weight'],
			'shelter_id': request.form['shelter_id']}
		models.editPuppy(edit_puppy, puppy_id)
		return redirect(url_for('puppies'))
	else:
		return render_template('puppyEdit.html', puppy = puppy, puppy_id = puppy_id, shelters = shelters, shelter = shelter)


#
@app.route('/puppies/<int:puppy_id>/puppydelete', methods = ['GET','POST'])
def puppyDelete(puppy_id):
	puppy = models.selectAllPuppies().filter_by(puppy_id=puppy_id)
	if request.method == "POST":
		models.deletePuppy(puppy_id)
		return redirect(url_for('puppies'))
	else:
		return render_template('puppyDelete.html', puppy = puppy, puppy_id = puppy_id)


