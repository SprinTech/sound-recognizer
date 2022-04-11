import requests
from .auth import check_token_status

# REQUEST OPERATIONS
def make_get_request(token, url, params={}):
    # headers = {"Authorization": f"Bearer {session['access_token']}"}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401 and check_token_status(token) is not None:
        return make_get_request(token, url, params)
    else:
        return None
    
def make_post_request(token, url, data):
    headers = {
        "Authorization": f"Bearer {token}", 
        'Accept': 'application/json', 
        'Content-Type': 'application/json'
        }
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 201:
        return response.json()
    elif response.status_code == 401 and check_token_status(token) is not None:
        return make_post_request(token, url, data)
    elif response.status_code == 403 or response.status_code == 404:
        return response.status_code
    else:
        return None

# SPOTIFY API REQUESTS
def get_user_information(token):
	url = 'https://api.spotify.com/v1/me'
	payload = make_get_request(token, url)

	if payload is None:
		return None

	return payload