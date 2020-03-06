import 'react-app-polyfill/ie11'
import 'react-app-polyfill/stable'
import React from 'react';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';

import axios from 'axios'

console.log(process.env)

const responseGoogle = (response) => {
  console.log(process.env)
  const url = `${process.env.REACT_APP_API_HOST}/auth/convert-token/`
  axios.post(url, {
    grant_type: 'convert_token',
    client_id: process.env.REACT_APP_OUR_OAUTH2_CLIENT_ID,
    client_secret: process.env.REACT_APP_OUR_OAUTH2_CLIENT_SECRET,
    backend: 'google-oauth2',
    token: response.accessToken
  })
  .then(function (response) {
      alert(`everything works. Your token is ${response.data.access_token}`)
  })
}

ReactDOM.render(
  <GoogleLogin
    clientId="106472885152-oh6gvqlopj4hjpotisfrh22qe8jpj27k.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={responseGoogle}
    onFailure={responseGoogle}
    cookiePolicy={'single_host_origin'}
  />,
  document.getElementById('root')
);

