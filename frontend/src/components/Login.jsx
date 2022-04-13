import React from 'react';
const Login = () => {
    return (
        <a href={`${process.env.AUTH_ENDPOINT}?client_id=${process.env.CLIENT_ID}&redirect_uri=${process.env.REDIRECT_URI}&response_type=${process.env.RESPONSE_TYPE}`}>
            Login to Spotify 
        </a>
        );
}

export default Login;