import 'react-app-polyfill/ie11'
import 'react-app-polyfill/stable'
import React from 'react';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';
import axios from 'axios'
 
 
const responseGoogle = (response) => {
  console.log(response);
  console.log(response.accessToken);
  const url = 'http://localhost:8000/auth/convert-token/'
  axios.post(url, {
    grant_type: 'convert_token',
    client_id: '5ysYYZ0vFkAvt25439LngkGN4aB84IWmYBx1C61G',
    client_secret: 'KX8QJZgEIZKeZJO6Ouz38Sd8smIngrEuAj4vOetgwIpQfgzSE7UKJOVXvi5bzdKsOj9W2OtS5n6Ndm1GO14VcubsZTX9KWNUYArthZ0hcwuMtZxLOF5hTYJ7BEGEQeEH',
    backend: 'google-oauth2',
    token: response.accessToken
  })
  .then(function (response) {
          console.log(response);
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

