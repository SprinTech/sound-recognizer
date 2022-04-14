from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from config import Settings
from routes import auth, user, playlist
import models
from database import engine

settings = Settings()

tags_metadata = [
    {
        "name": "Spotify",
        "description": "Operations using Spotify API integration",
        "externalDocs": {
            "description": "Spotify external docs",
            "url": "https://developer.spotify.com/documentation/"
        }
    }
]

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Sound recognizer API",
    description = "This API allow user to get genre prediction according to Spotify music supplied to app",
    version = "0.1",
    openapi_tags = tags_metadata
)

app.include_router(auth.router, tags=["authentication"], prefix="/api/v1")
app.include_router(playlist.router, tags=["playlist"], prefix="/api/v1")
app.include_router(user.router, tags=["user"], prefix="/api/v1")

@app.get("/api/v1/")
async def root():
    return {"message": "Hello World !"}

@app.get("/api/v1/logout")
async def logout():
    response = RedirectResponse(url="/api/v1/")
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    response.delete_cookie(key="token_expiration")
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, debug=True, reload=True)