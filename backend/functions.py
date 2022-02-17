import random as rand
import string as string
import requests
import logging
from main import create_app
import time

app = create_app()

def createStateKey(size):
    # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    return ''.join(rand.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))

def refreshToken(refresh_token):
    token_url = 'https://accounts.spotify.com/api/token'
    authorization = app.config['AUTHORIZATION']

    headers = {
        'Authorization': authorization,
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = {
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }
    post_response = requests.post(token_url, headers=headers, data=body)

    # 200 code indicates access token was properly granted
    if post_response.status_code == 200:
        return post_response.json()['access_token'], post_response.json()['expires_in']
    else:
        logging.error('refreshToken:' + str(post_response.status_code))
        return None

def getToken(code):
    token_url = 'https://accounts.spotify.com/api/token'
    authorization = app.config['AUTHORIZATION']
    redirect_uri = app.config['REDIRECT_URI']
    headers = {
        'Authorization': authorization,
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = {
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    post_response = requests.post(token_url,headers=headers,data=body)
    if post_response.status_code == 200:
        pr = post_response.json()
        return pr['access_token'], pr['refresh_token'], pr['expires_in']
    else:
        logging.error('getToken:' + str(post_response.status_code))
    return None


def checkTokenStatus(session):
    if time.time() > session['token_expiration']:
        payload = refreshToken(session['refresh_token'])
        # FIXME comparison to None should be 'if cond' or 'if cond is not None:'
        if payload != None:
            session['token'] = payload[0]
            session['token_expiration'] = time.time() + payload[1]
        else:
            logging.error('checkTokenStatus')
            return None

    return "Success"


def makeGetRequest(session, url, params={}):
    headers = {"Authorization": "Bearer {}".format(session['token'])}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401 and checkTokenStatus(session) != None:
        return makeGetRequest(session, url, params)
    else:
        logging.error('makeGetRequest:' + str(response.status_code))
    return None


def getUserInformation(session):
    url = 'https://api.spotify.com/v1/me'
    payload = makeGetRequest(session, url)

    # FIXME comparison to None should be 'if cond' or 'if cond is not None:'
    if payload == None:
        return None

    return payload


def getAllTopTracks(session, limit=10):
    url = 'https://api.spotify.com/v1/me/top/tracks'
    track_ids = []
    time_range = ['short_term', 'medium_term', 'long_term']

    for time in time_range:
        track_range_ids = []

        params = {'limit': limit, 'time_range': time}
        payload = makeGetRequest(session, url, params)

        # FIXME comparison to None should be 'if cond' or 'if cond is not None:'
        if payload == None:
            return None

        for track in payload['items']:
            track_range_ids.append(track['id'])

        track_ids.append(track_range_ids)

    return track_ids
