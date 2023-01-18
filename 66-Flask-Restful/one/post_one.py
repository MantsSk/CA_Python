import requests
import json

r = requests.get('http://127.0.0.1:8000/leap/2028')
dictionary = json.loads(r.text)
print(dictionary['result'])
