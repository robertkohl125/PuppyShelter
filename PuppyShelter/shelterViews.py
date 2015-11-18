from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/shelters')
def shelters():
    shelters = models.selectAllShelters()
    return render_template('shelterAll.html', shelters = shelters)


#
@app.route('/shelters/shelterview', methods = ['GET','POST'])
def shelterView():
    shelter = models.selectShelter()
    return render_template('shelterView.html', shelters = shelters)


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
    return 'shelteredit'


#
@app.route('/shelters/<int:shelter_id>/shelterdelete', methods = ['GET','POST'])
def shelterDelete(shelter_id):
    return 'shelterdelete'