import requests

def random_cat(quantity):
    for i in range(quantity):
        r = requests.get('https://cataas.com/cat')
        with open(f'cat{i}.jpg', 'wb') as file:
            file.write(r.content)

random_cat(2)