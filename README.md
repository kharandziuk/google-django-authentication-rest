# TO RUN
* install docker
* Create an app and obtain credentials https://developers.google.com/identity/protocols/OAuth2 
  * https://console.developers.google.com/ 
  * credential tab 
  * create credentials for Web App
  * REDIRECT_URI is http://localhost:8000/complete/google-oauth2/
  * JavaScript origin http://localhost:3000
* copy dotenv.example into .env
* put propper credentials in .env
* run `docker-compose up`
* localhost:8000 -> non-spa version
* localhost:3000 -> spa and rest
