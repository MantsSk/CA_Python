import requests
import json

payload = {'vardas': 'Donatas', 'pavarde': 'Noreika', 'amzius': 2000,
           'jwt': "fasdfat5435bgfdlkgjj54k354b",
           }
r = requests.post('http://127.0.0.1:5000/', json=payload, timeout=1)
dictionary = json.loads(r.text)
print(dictionary)
