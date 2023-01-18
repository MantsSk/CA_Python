import requests
import json

payload = {'name': 'Jonas', 'surname': 'Petras', 'age': 2000}
r = requests.post('http://127.0.0.1:8000/', json=payload)
dictionary = json.loads(r.text)
print(dictionary)

# {'you sent': {'name': 'Jonas', 'surname': 'Petras', 'age': 2000}}
