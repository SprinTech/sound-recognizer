from .request_methods import make_get_request

def get_user_information(session):
    """
    Return Spotify username
    """
    url = 'https://api.spotify.com/v1/me'
    payload = make_get_request(session, url)

    if payload is None:
        return None

    return payload

def get_user_playlist(session, limit=10):
    """
    Connect to user playlist in Spotify and 
    """
    url = 'https://api.spotify.com/v1/me/playlists'
    offset = 0
    playlist = []
    
    total = 1
    while total > offset:
        params = {'limit': limit, 'offset': offset}
        payload = make_get_request(session, url, params)
        
        if payload is None:
            return None
        
        for item in payload['items']:
            playlist.append([item['name'], item['uri']])

        total = payload['total']
        offset += limit
    
    return payload

def get_user_tracks(session, limit=10):
    pass