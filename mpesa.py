import requests
import base64
from datetime import datetime

timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
business_shortcode_test = "174379"
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

password = business_shortcode_test + passkey + timestamp

otp = base64.b64encode(password.encode())
decode_otp = otp.decode('utf-8')

access_token = "KMt35ArPbWPgC4HXXo3G3HprgGSK"
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = {"Authorization": "Bearer %s" % access_token}

request = {"BusinessShortCode":"174379",
            "Password": decode_otp,
            "Timestamp": timestamp,    
            "TransactionType": "CustomerBuyGoodsOnline",
            "Amount":"1",    
            "PartyA":"254700014463",    
            "PartyB":"174379",    
            "PhoneNumber":"254700014463",    
            "CallBackURL":"https://79372821.ngrok.io/api/v1/c2b/confirmation",    
            "AccountReference":"Transacty",    
            "TransactionDesc":"Pay Transacty"
}


response = requests.post(api_url, json = request, headers=headers)
print (response.text)
