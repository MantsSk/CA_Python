import requests

payload = {'q': 'pep', 'page': '2', 'submit': ''}
r = requests.get('https://www.python.org/search/', params=payload)
print(r.url)

data = {'name': 'Jonas', 'lastname': 'Jonaitis'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
