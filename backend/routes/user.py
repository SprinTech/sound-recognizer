import sys
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

sys.path.append("..")
from config import Settings
from controllers.playlist import get_user_playlist, get_user_songs

settings = Settings()
router = APIRouter()


@router.get("/playlist/")
async def user_playlist(request: Request):
    access_token = request.cookies.get("access_token")
    playlist_names = get_user_playlist(access_token)
    return JSONResponse(playlist_names)

@router.get("/songs/")
async def user_songs(request: Request):
    access_token = request.cookies.get("access_token")
    
    # retrieve ids of user playlist
    playlist_ids = get_user_playlist(access_token)
    song_list = []
    
    for playlist in playlist_ids['items']:
        id = playlist['id']
        songs = get_user_songs(id, access_token)
        song_list.append(songs)
    
    # return JSONResponse(song_list)
    return song_list