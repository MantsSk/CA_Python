import requests

people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)
