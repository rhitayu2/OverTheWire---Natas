import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()

url="http://natas11.natas.labs.overthewire.org"

username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

req = session.get(url, auth=HTTPBasicAuth(username, password))

print(req.text)