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
    playlist_id = []
    
    total = 1
    while total > offset:
        params = {'limit': limit, 'offset': offset}
        payload = make_get_request(session, url, params)
        
        if payload is None:
            return None
        
        for item in payload['items']:
            playlist_id.append(item['id'])

        total = payload['total']
        offset += limit

    return payload

def get_user_songs(playlist_id, session, limit=10):
    """
    Connect to user playlist in Spotify and 
    """
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    
    offset = 0
    song_preview = []
    
    total = 1
    
    while total > offset:
        params = {'limit': limit, 'offset': offset}
        payload = make_get_request(session, url, params)
        
        if payload is None:
            return None
        
        for item in payload['items']:
            song_preview.append(item['track']['preview_url'])

        total = payload['total']
        offset += limit
        
    return song_preview