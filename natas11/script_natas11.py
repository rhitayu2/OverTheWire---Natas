import requests
from requests.auth import HTTPBasicAuth
import base64
import urllib.parse

url="http://natas11.natas.labs.overthewire.org"
username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"


session = requests.Session()

cookie = {
	"data":"ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMM"
}

data = {
	"bgcolor":"#ffffff"
}

session.cookies['data']='ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMM'
req = session.post(url, auth=HTTPBasicAuth(username, password))
print(req.cookies)
# xor_encrypt(1)


# print(req.text)