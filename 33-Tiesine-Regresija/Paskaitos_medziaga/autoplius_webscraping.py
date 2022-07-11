import requests
from my_headers import get_headers

headers = get_headers()
s = requests.Session()
#resp = s.get("https://autoplius.lt/skelbimai/naudoti-automobiliai?offer_type=0", headers=headers)
r = requests.get("https://autoplius.lt/skelbimai/naudoti-automobiliai?offer_type=0", headers=headers)
pass
