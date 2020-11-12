import requests
from requests.auth import HTTPBasicAuth

url = "http://natas12.natas.labs.overthewire.org/"
username = "natas12"
password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"

session = requests.Session()

req = session.get(url, auth = HTTPBasicAuth(username, password))

print(req.text)