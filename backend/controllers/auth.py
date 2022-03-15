import string as string
import random as rand
import time
import base64
import requests

from main import app

def create_state_key(size):
    return ''.join(rand.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))

def get_token(code, state):
    redirect_uri = app.config["REDIRECT_URI"]
    client_credential = app.config["AUTHORIZATION"]
    client_credential_b64 = base64.b64encode(client_credential.encode())
    
    if not state:
        return "Error, state missing..."
    else:
        token_url = 'https://accounts.spotify.com/api/token'
        headers =  {
            "Authorization": f"Basic {client_credential_b64.decode()}",
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
            }
        body = {
                "code": code,
                "redirect_uri": redirect_uri,
                "grant_type": "authorization_code" 
            }
        
        response = requests.post(token_url, headers=headers, data=body)
        return response.json()

def get_refresh_token(refresh_token):
    client_credential = app.config["AUTHORIZATION"]
    client_credential_b64 = base64.b64encode(client_credential.encode())
    
    token_url = 'https://accounts.spotify.com/api/token'
    headers =  {
            "Authorization": f"Basic {client_credential_b64.decode()}",
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
            }
    body = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    
    response = requests.post(token_url, headers=headers, data=body)
    return response.json()

def check_token_status(session):
    if time.time() > session["token_expiration"]:
        payload = get_refresh_token(session["refresh_token"])
        
        if payload is not None:
            session["access_token"] = payload["access_token"]
            session["token_expiration"] = time.time() + payload["expires_in"]