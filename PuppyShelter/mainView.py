from PuppyShelter import app
from PuppyShelter import models
from flask import render_template, url_for, request, redirect, flash, jsonify


#
@app.route('/')
def main():
    return render_template('main.html')


#
@app.route('/puppies/<int:puppy_id>/adopt', methods = ['GET','POST'])
def puppyAdopt(puppy_id):
    return 'adoption page'