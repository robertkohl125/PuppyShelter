from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/puppies/')
def puppies():
    puppies = models.selectAllPuppies()
    return render_template('puppyAll.html', puppies = puppies)


#
@app.route('/puppies/<int:puppy_id>/puppyview', methods = ['GET','POST'])
def puppyView(puppy_id):
    return 'puppyview'


#
@app.route('/puppies/puppynew', methods = ['GET','POST'])
def puppyNew():
	shelters = models.selectAllShelters()
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
		return render_template('puppyNew.html', shelters = shelters)


#
@app.route('/puppies/<int:puppy_id>/puppyedit', methods = ['GET','POST'])
def puppyEdit(puppy_id):
    return 'puppyedit'


#
@app.route('/puppies/<int:puppy_id>/puppydelete', methods = ['GET','POST'])
def puppyDelete(puppy_id):
	puppy = models.selectAllPuppies().filter_by(puppy_id=puppy_id)
	if request.method == "POST":
		models.deletePuppy(puppy_id)
		return redirect(url_for('puppies'))
	else:
		return render_template('puppyDelete.html', puppy = puppy, puppy_id = puppy_id)


