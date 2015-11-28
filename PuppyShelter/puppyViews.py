from PuppyShelter import app, models, forms
from flask import render_template, url_for, request, redirect, flash, jsonify
import logging 


logging.info('puppyViews.py file accessed ')

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
		txt1 = 'Adopt'
		txt2 = ''
		btn = 'success'
		att = 'enabled'
	else:
		txt1 = ''
		txt2 = 'was already adopted'
		btn = 'danger'
		att = 'disabled'
	return render_template('puppyView.html', 
		puppy = puppy, 
		puppy_id = puppy_id, 
		shelter = shelter, 
		owner = owner, 
		txt1 = txt1,
		txt2 = txt2,
		att = att, 
		btn = btn)


#
@app.route('/puppies/puppynew', methods = ['GET','POST'])
def puppyNew():
	shelter_choices = models.selectAvailableShelters()
	form = forms.PuppyForm(request.form, obj = shelter_choices)
	form.shelter_id.choices = [(a.shelter_id, a.name) for a in shelter_choices]
	print form.shelter_id.choices
	if request.method == "POST" and form.validate():
		new_puppy = {
			'name': form.name.data,
			'gender': form.gender.data,
			'dateOfbirth': form.dateOfbirth.data,
			'picture': form.picture.data,
			'breed': form.breed.data,
			'weight': form.weight.data,
			'shelter_id': form.shelter_id.data}
		models.createPuppy(new_puppy)
		flash('A new puppy is ready for adoption!')
		return redirect(url_for('puppies'))
	else:
		return render_template('puppyNew.html', 
			form = form)


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
		return render_template('puppyEdit.html', 
			puppy = puppy, 
			puppy_id = puppy_id, 
			shelters = shelters, 
			shelter = shelter)


#
@app.route('/puppies/<int:puppy_id>/puppydelete', methods = ['GET','POST'])
def puppyDelete(puppy_id):
	puppy = models.selectAllPuppies().filter_by(puppy_id=puppy_id)
	if request.method == "POST":
		models.deletePuppy(puppy_id)
		return redirect(url_for('puppies'))
	else:
		return render_template('puppyDelete.html', 
			puppy = puppy, 
			puppy_id = puppy_id)

app.secret_key = 'super_secret_key'