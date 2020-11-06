import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()

url = "http://natas6.natas.labs.overthewire.org/"

username="natas6"
password="aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

data = {
	"secret":"FOEIUWGHFEEUHOFUOIU",
	"submit":"Submit Query"
}

req = session.post(url, auth=HTTPBasicAuth(username, password), data=data)

print(req.text)