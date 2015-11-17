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
    return render_template('shelterNew.html', shelters = shelters)


#
@app.route('/shelters/<int:shelter_id>/shelteredit', methods = ['GET','POST'])
def shelterEdit(shelter_id):
    return 'shelteredit'


#
@app.route('/shelters/<int:shelter_id>/shelterdelete', methods = ['GET','POST'])
def shelterDelete(shelter_id):
    return 'shelterdelete'