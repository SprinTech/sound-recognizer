import React from 'react';

const CLIENT_ID = "a9284e79d32640229c58154c0cc822ba"
const REDIRECT_URI = "http://127.0.0.1:5000/api/v1/callback/"
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