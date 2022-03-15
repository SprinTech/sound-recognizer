from flask import redirect, request, session, make_response, Blueprint, current_app
import urllib.parse
import sys
sys.path.append("..")

from controllers.auth import create_state_key, get_token
from controllers.playlist import get_user_information

auth_blueprint = Blueprint('auth', __name__, template_folder="templates")

@auth_blueprint.route("/authorize/")
def authorize():
    """
    Request authorization from the user to access it's Spotify ressources
    """
    # Import api configs
    client_id = current_app.config["CLIENT_ID"]
    client_secret = current_app.config["CLIENT_SECRET"]
    redirect_uri = current_app.config["REDIRECT_URI"]
    scope = current_app.config["SCOPE"]
    
    state = create_state_key(16)
    
    authorization_url = 'https://accounts.spotify.com/authorize?'
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'redirect_uri': redirect_uri,
        'state': state
    }
    
    encoded_params = urllib.parse.urlencode(params)
    response = make_response(redirect(authorization_url + encoded_params))
    return response

@auth_blueprint.route("/callback/")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    payload = get_token(code, state)
    
    if payload is not None:
        session["access_token"] = payload["access_token"]
        session["refresh_token"] = payload["refresh_token"]
        session["token_expiration"] = payload["expires_in"]
    
    current_user = get_user_information(session)
    session["user_id"] = current_user["id"]
    return session["user_id"]