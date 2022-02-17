from flask import render_template, redirect, request, session, make_response
import time
import logging

from functions import createStateKey, getToken, getUserInformation, getAllTopTracks
from main import create_app

app = create_app()

@app.route("/")
def hello():
    return "Hello, World"

@app.route('/auth')
def authorize():
	client_id = app.config['CLIENT_ID']
	client_secret = app.config['CLIENT_SECRET']
	redirect_uri = app.config['REDIRECT_URI']
	scope = app.config['SCOPE']

	# state key used to protect against cross-site forgery attacks
	state_key = createStateKey(15)
	session['state_key'] = state_key

	# redirect user to Spotify authorization page
	authorize_url = 'https://accounts.spotify.com/en/authorize?'
	parameters = 'response_type=code&client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&scope=' + scope + '&state=' + state_key
	response = make_response(redirect(authorize_url + parameters))
	return response

@app.route('/callback')
def callback():
	# make sure the response came from Spotify
	if request.args.get('state') != session['state_key']:
		return render_template('index.html', error='State failed.')
	if request.args.get('error'):
		return render_template('index.html', error='Spotify error.')
	else:
		code = request.args.get('code')
		session.pop('state_key', None)

		# get access token to make requests on behalf of the user
		payload = getToken(code)
		if payload != None:
			session['token'] = payload[0]
			session['refresh_token'] = payload[1]
			session['token_expiration'] = time.time() + payload[2]
		else:
			return render_template('index.html', error='Failed to access token.')

	current_user = getUserInformation(session)
	session['user_id'] = current_user['id']
	logging.info('new user:' + session['user_id'])

	return redirect(session['previous_url'])

@app.route('/tracks',  methods=['GET'])
def tracks():
	# make sure application is authorized for user 
	if session.get('token') == None or session.get('token_expiration') == None:
		session['previous_url'] = '/tracks'
		return redirect('/authorize')

	# collect user information
	if session.get('user_id') == None:
		current_user = getUserInformation(session)
		session['user_id'] = current_user['id']

	track_ids = getAllTopTracks(session)

	if track_ids == None:
		return render_template('index.html', error='Failed to gather top tracks.')
		
	return render_template('tracks.html', track_ids=track_ids)

if __name__ == "__main__":
    app.run()