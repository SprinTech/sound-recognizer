import urllib.parse
import sys
from fastapi import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse
sys.path.append("..")

from controllers.auth import create_state_key, get_token
from controllers.playlist import get_user_information
# from controllers.user import create_user
from config import Settings

settings = Settings()
router = APIRouter()


@router.get("/authorize/")
def authorize():
    """
    Request authorization from the user to access it's Spotify ressources
    """
    # Import api configs
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    redirect_uri = settings.REDIRECT_URI
    scope = settings.SCOPE
    
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
    response = RedirectResponse(authorization_url + encoded_params)
    return response

@router.get("/callback/")
async def callback(code: str, state: str):
    redirect_uri = settings.REDIRECT_URI
    client_credential = settings.AUTHORIZATION
    payload = get_token(code, state, redirect_uri, client_credential)

    current_user = get_user_information(payload["access_token"])
        
    json_user =  JSONResponse(current_user)
    
    if payload is not None:
        json_user.set_cookie(key="access_token", value=payload["access_token"])
        json_user.set_cookie(key="refresh_token", value=payload["refresh_token"])
        json_user.set_cookie(key="token_expiration", value=payload["expires_in"])

    json_user.set_cookie(key="access_token", value=payload["access_token"])

    return json_user