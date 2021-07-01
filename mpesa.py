import requests
from requests.auth import HTTPBasicAuth
import base64
from datetime import datetime

consumer_key = "7TTD0aMGv0ARkAjMFCAdblAUDBvTdpcM"
consumer_secret = "HL32esQQ6Fn0twr9"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

access_token = 'iARKpGqcGE8uFpmsWD4bRtqAHESL'
api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
headers = {"Authorization": "Bearer %s" % access_token}

request = { "Initiator":"georgeey",
      "SecurityCredential":"TRU6o8vGrgE5qd5uveWKB/RAnRaFQofrG/oSuu3q6Lw7LXDKcZfK6Cum6fUAm+A17DSyq+2YjIpWBoGAa/AICSrN0eD4rDU0qs9UUeDLc8tTOi2GZoGxcjg1XzUtav5EC5IOmznr0wtFOLcW/abgRWgjLyykn7LlVCKNieWciaFkpsyUiHXJy+C/Cv35QatL5YeAN4HddnaduKMbrMf+hahbQSsrjBD+PdHZeqPuHXBiLy1EcRTVrGFXMftqhT8+TpJHq8TGg/zbJuctb2WcaGAhpqjgIJvg5KjwnbB65gFbxFGBBdedS58b/IAXyqLdio0BrPWvlT9rKxB6sebDcg==",
      "CommandID":"AccountBalance",
      "PartyA":"174379",
      "IdentifierType":"4",
      "Remarks":"first trial is a success",
      "QueueTimeOutURL":"https://e765deaff768.ngrok.io/",
      "ResultURL":"https://e765deaff768.ngrok.io/"
      }

response = requests.post(api_url, json = request, headers=headers)
print (response.text)