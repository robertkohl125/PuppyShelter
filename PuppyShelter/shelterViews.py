from PuppyShelter import app, models, forms
from flask import render_template, url_for, request, redirect, flash, jsonify
import logging 
from flask import session as login_session


logging.info('shelterViews.py file accessed ')

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



@app.route('/shelters/shelternew', methods = ['GET','POST'])
def shelterNew():
    if 'username' not in login_session:
        return render_template('unauthorized.html')
    else:
		form = forms.ShelterForm(request.form)
		if request.method == "POST" and form.validate():
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
    if 'username' not in login_session:
        return render_template('unauthorized.html')
    else:
		form = forms.ShelterForm()
		shelter = models.selectAllShelters().filter_by(shelter_id=shelter_id)
		if request.method == "POST" and form.validate():
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
			return render_template('shelterEdit.html', 
				shelter_id = shelter_id, 
				shelter = shelter, 
				form = form)


#
@app.route('/shelters/<int:shelter_id>/shelterdelete', methods = ['GET','POST'])
def shelterDelete(shelter_id):
    if 'username' not in login_session:
        return render_template('unauthorized.html')
    else:
		shelter = models.selectAllShelters().filter_by(shelter_id=shelter_id)
		if request.method == "POST":
			models.deleteShelter(shelter_id)
			flash('A new shelter has been deleted!')
			return redirect(url_for('shelters'))
		else:
			return render_template('shelterDelete.html', shelter = shelter, shelter_id = shelter_id)

# set the secret key.
app.secret_key = 'super_secret_key'