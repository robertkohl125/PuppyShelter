from PuppyShelter import app, models, sms, email
from flask import render_template, url_for, request, redirect, flash, jsonify
import logging 


logging.info('mainView.py file accessed ')

#
@app.route('/')
def main():
    return render_template('main.html')


#
@app.route('/<int:puppy_id>/adopt/', methods = ['GET','POST'])
def puppyAdopt(puppy_id):
	puppy = models.selectAllPuppies().filter_by(puppy_id=puppy_id)
	for pup in puppy:
		shelt = pup.shelter_id
	owners = models.selectAllOwners()
	shelters = models.selectAllShelters().filter_by(shelter_id=shelt)
	a = models.selectAdopterOwners(puppy_id).scalar()
	if a is None:
		txt1 = 'Adopt'
		txt2 = 'now!'
		btn = 'success'
		att = 'enabled'
	else:
		txt1 = ''
		txt2 = 'was already adopted'
		btn = 'danger'
		att = 'disabled'
	if request.method == "POST":
		dict_ownr = {'owner_id': request.form['owner_id']}
		print dict_ownr
		ownr = dict_ownr.get('owner_id')
		models.adoptPuppy(puppy_id, ownr, shelt)
		text = ('puppy_id(%s) was adopted from shelter_id(%s) by owner_id(%s)' % (puppy_id, ownr, shelt))
		logging.info = text
		text = text
		r = owners.filter_by(owner_id=ownr)
		for r in r:
			print r
		recipient = r.email
		email.email(text,recipient)
		return redirect(url_for('puppies'))
	else:
		return render_template('adoptPuppy.html', 
			puppy = puppy, 
			owners = owners, 
			shelters = shelters, 
			txt1 = txt1,
			txt2 = txt2,
			att = att, 
			btn = btn)


app.secret_key = 'super_secret_key'