import requests
from bs4 import BeautifulSoup

r = requests.get('https://orai.15min.lt/prognozes')
html = r.text

soup = BeautifulSoup(html, "html.parser")
temperature_list = soup.find_all(class_="item full clearfix")

for temperature in temperature_list:
    temp = temperature.select(".temperature")[0].get_text().strip()
    city = temperature.select('.city')[0].get_text().strip()

    print(f"{city} has {temp} temperature")

# split_by_vilnius = html.split('Vilnius')
#
# split_by_hot = split_by_vilnius[-1].split('hot">')
# res = split_by_hot[1].split()[0]
#
# print(res)