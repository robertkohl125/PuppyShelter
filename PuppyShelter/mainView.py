from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify
import logging


logging.basicConfig(filename='pslog.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

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
		att = 'enabled'
	else:
		att = 'disabled'
	if request.method == "POST":
		dict_ownr = {'owner_id': request.form['owner_id']}
		print dict_ownr
		ownr = dict_ownr.get('owner_id')
		models.adoptPuppy(puppy_id, ownr, shelt)
		return redirect(url_for('puppies'))
		logging.info = ('puppy_id(%s) was adopted from shelter_id(%s) by owner_id(%s)',puppy_id, ownr, shelt)
	else:
		return render_template('adoptPuppy.html', 
			puppy = puppy, owners = owners, shelters = shelters, att = att)