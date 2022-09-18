import requests
import json

payload = {'pavadinimas': 'Call grandma', 'atlikta': True}
r = requests.post('http://127.0.0.1:8000/uzduotis', json=payload, timeout=1)
dictionary = json.loads(r.text)
print(dictionary)
