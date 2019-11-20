import requests


r = requests.get('http://httpbin.org/delay/3', auth=('kevin', 'testing'), timeout=3)

print(r.text)
