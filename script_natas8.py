import requests
from requests.auth import HTTPBasicAuth
import binascii
import base64

session = requests.Session()

url = "http://natas8.natas.labs.overthewire.org/"

username="natas8"
password="DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

encoded_secret = "3d3d516343746d4d6d6c315669563362"
encoded_secret =  binascii.unhexlify(encoded_secret)[::-1]
encoded_secret =  base64.b64decode(encoded_secret).decode("utf-8")

# print(encoded_secret)

data = {
	"secret":encoded_secret,
	"submit":"1"
}

req = session.post(url, auth=HTTPBasicAuth(username, password), data=data)

print(req.text)
# print(req.url)
