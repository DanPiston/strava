import config

from requests_oauthlib import OAuth2Session
from pprint import pprint

strava = OAuth2Session(access_token=config.access_token)
response = strava.get('https://wwww.strava.com/api/v3/athlete')

print(response)
