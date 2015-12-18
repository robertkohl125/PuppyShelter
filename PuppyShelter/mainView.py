from PuppyShelter import app, models
from components import sms, email
from flask import render_template, url_for, request, redirect, flash, jsonify
import logging 

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from requests_oauthlib import OAuth2Session
import httplib2
import json
from flask import make_response
import requests

logging.info('mainView.py file accessed ')

CLIENT_ID = json.loads(open('secrets/g_client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "PuppyShelter"


#
@app.route('/main')
def main():
    return render_template('main.html')


#
@app.route('/login', methods=['GET', 'POST'])
def showLogin():
    #Create state token
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('main'))
    return render_template('login.html', error=error, STATE = state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    #Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data
    try:
        oauth_flow = flow_from_clientsecrets('secrets/g_client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
        response = make_response(
            json.dumps(result.get('error')), 50)
        response.headers['Content-Type'] = 'application/json'
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID does not match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps("Current user is already connected."), 200)
        response.headers['Content-Type'] = 'application/json'
    
    login_session['provider'] = 'google'
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = models.getUserID(login_session['email'])
    if user_id is None:
        user_id = models.createUser(login_session)
    else:
        login_session['user_id'] = user_id

    output = ''
    output += '<h2>Welcome Google+ user '
    output += login_session['username']
    output += '!</h2>'
    output += '<h4><b>gplus_id:</b>'
    output += login_session['gplus_id']
    output += '<br>'
    output += '<b>credentials:</b>'
    output += login_session['credentials']
    output += '<br>'
    output += '<b>email:</b>'
    output += login_session['email']
    output += '<br>'
    output += '</h4>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius:\
     150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route("/gdisconnect")
def gdisconnect():
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        return response


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


#
app.secret_key = 'super_secret_key'