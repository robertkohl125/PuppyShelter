from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/shelters/')
def shelters():
    shelters = models.selectAllShelters()
    for s in shelters:
    	mc = s.maximum_capacity
    	co = s.current_occupancy
    rems = mc - co
    return render_template('shelterAll.html', shelters = shelters, rem = rems)


#
@app.route('/shelters/<int:shelter_id>/shelterview/')
def shelterView(shelter_id):
    shelter = models.selectShelter(shelter_id)
    puppies = models.selectPuppiesByShelter(shelter_id)
    return render_template('shelterView.html', shelter = shelter, puppies = puppies)


#
@app.route('/shelters/shelternew', methods = ['GET','POST'])
def shelterNew():
	if request.method == "POST":
		new_shelter = {'name': request.form['name'],
			'address': request.form['address'],
			'city': request.form['city'],
			'state': request.form['state'],
			'zipCode': request.form['zipCode'],
			'website': request.form['website'],
			'maximum_capacity': request.form['maximum_capacity']}
		models.createShelter(new_shelter)
		return redirect(url_for('shelters'))
	else:
		return render_template('shelterNew.html')


#
@app.route('/shelters/<int:shelter_id>/shelteredit', methods = ['GET','POST'])
def shelterEdit(shelter_id):
	shelter = models.selectAllShelters().filter_by(shelter_id=shelter_id)
	if request.method == "POST":
		edit_shelter = {'name': request.form['name'],
			'address': request.form['address'],
			'city': request.form['city'],
			'state': request.form['state'],
			'zipCode': request.form['zipCode'],
			'website': request.form['website'],
			'maximum_capacity': request.form['maximum_capacity']}
		models.editShelter(edit_shelter, shelter_id)
		return redirect(url_for('shelters'))
	else:
		return render_template('shelterEdit.html', shelter_id = shelter_id, shelter = shelter)


#
@app.route('/shelters/<int:shelter_id>/shelterdelete', methods = ['GET','POST'])
def shelterDelete(shelter_id):
	shelter = models.selectAllShelters().filter_by(shelter_id=shelter_id)
	if request.method == "POST":
		models.deleteShelter(shelter_id)
		return redirect(url_for('shelters'))
	else:
		return render_template('shelterDelete.html', shelter = shelter, shelter_id = shelter_id)