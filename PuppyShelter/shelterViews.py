from PuppyShelter import app
from PuppyShelter import models
from PuppyShelter import forms
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/shelters/')
def shelters():
	shelters = models.selectAllShelters()
	return render_template('shelterAll.html', shelters = shelters)


#
@app.route('/shelters/<int:shelter_id>/shelterview/')
def shelterView(shelter_id):
    shelter = models.selectShelter(shelter_id)
    puppies = models.selectPuppiesByShelter(shelter_id)
    return render_template('shelterView.html', shelter = shelter, puppies = puppies)


#
@app.route('/shelters/shelternew', methods = ['GET','POST'])
def shelterNew():
	form = forms.ShelterForm()
	if request.method == "POST":
		new_shelter = {
			'name': form.name.data,
			'address': form.address.data,
			'city': form.city.data,
			'state': form.state.data,
			'zipCode': form.zipCode.data,
			'website': form.website.data,
			'maximum_capacity': form.maximum_capacity.data}
		models.createShelter(new_shelter)
		flash('A new shelter has been opened!')
		return redirect(url_for('shelters'))
	else:
		return render_template('shelterNew.html', form = form)


#
@app.route('/shelters/<int:shelter_id>/shelteredit', methods = ['GET','POST'])
def shelterEdit(shelter_id):
	form = forms.ShelterForm()
	shelter = models.selectAllShelters().filter_by(shelter_id=shelter_id)
	if request.method == "POST":
		edit_shelter = {
			'name': form.name.data,
			'address': form.address.data,
			'city': form.city.data,
			'state': form.state.data,
			'zipCode': form.zipCode.data,
			'website': form.website.data,
			'maximum_capacity': form.maximum_capacity.data}
		models.editShelter(edit_shelter, shelter_id)
		flash('A shelter has been edited!')
		return redirect(url_for('shelters'))
	else:
		return render_template('shelterEdit.html', shelter_id = shelter_id, shelter = shelter, form = form)


#
@app.route('/shelters/<int:shelter_id>/shelterdelete', methods = ['GET','POST'])
def shelterDelete(shelter_id):
	shelter = models.selectAllShelters().filter_by(shelter_id=shelter_id)
	if request.method == "POST":
		models.deleteShelter(shelter_id)
		flash('A new shelter has been deleted!')
		return redirect(url_for('shelters'))
	else:
		return render_template('shelterDelete.html', shelter = shelter, shelter_id = shelter_id)