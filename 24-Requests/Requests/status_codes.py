import requests

r = requests.get('http://python.org/')
if r.status_code not in range(400, 600):
    print('Pavyko prisijungti! Dirbame toliau...')
else:
    print(f'Kažkas ne taip.. Kodas {r.status_code}')

r = requests.get('http://shorturl.at/crN12')
if r.ok:
    print('važiuojam toliau!')
else:
    print(f'Klaida! kodas {r.status_code}')
