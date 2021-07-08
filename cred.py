import requests
from requests.auth import HTTPBasicAuth

access_token = "access_token"
api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
headers = {"Authorization": "Bearer %s" % access_token}

request = { "Initiator":"georgeey",
    "SecurityCredential":"TRU6o8vGrgE5qd5uveWKB/RAnRaFQofrG/oSuu3q6Lw7LXDKcZfK6Cum6fUAm+A17DSyq+2YjIpWBoGAa/AICSrN0eD4rDU0qs9UUeDLc8tTOi2GZoGxcjg1XzUtav5EC5IOmznr0wtFOLcW/abgRWgjLyykn7LlVCKNieWciaFkpsyUiHXJy+C/Cv35QatL5YeAN4HddnaduKMbrMf+hahbQSsrjBD+PdHZeqPuHXBiLy1EcRTVrGFXMftqhT8+TpJHq8TGg/zbJuctb2WcaGAhpqjgIJvg5KjwnbB65gFbxFGBBdedS58b/IAXyqLdio0BrPWvlT9rKxB6sebDcg==",
    "CommandID":"AccountBalance",
    "PartyA":"174379",
    "IdentifierType":"4",
    "Remarks":"first trial is a success",
    "QueueTimeOutURL":"http://portfoliombugua.herokuapp.com/",
    "ResultURL":"http://portfoliombugua.herokuapp.com/"
    }

response = requests.post(api_url, json = request, headers=headers)
print(response.text)