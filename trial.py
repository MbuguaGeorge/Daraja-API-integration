import requests
from requests.auth import HTTPBasicAuth
import json

consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print(r.text)