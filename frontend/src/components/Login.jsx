import React from 'react';

const CLIENT_ID = "+++++++++++++++++++++++++++++"
const REDIRECT_URI = "http://localhost:3000"
const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize"
const RESPONSE_TYPE = "token"

const Login = () => {
    return (
        <a href={`${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}`}>
            Login to Spotify
        </a>
    );
}

export default Login;