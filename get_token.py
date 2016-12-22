from pprint import pprint
import config
from requests_oauthlib import OAuth2Session

#Credentials
client_id = config.client_id
client_secret = config.client_secret 
redirect_uri = 'https://localhost'
token_url = 'https://www.strava.com/oauth/token'
approval_prompt='force'

auth_url = 'https://www.strava.com/oauth/authorize?approval_prompt=force'

response_type = 'code'

def get_auth():
    strava = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = strava.authorization_url(auth_url)
    print('Please go here', authorization_url)

    redirect_response = input('Paste the full redirect URL here:')

    access = strava.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)
    pprint(access)

def get_ath():
    strava = OAuth2Session(client_id)
    r = strava.get('https://www.strava.com/api/v3/athlete')
    print(r)

get_auth()
