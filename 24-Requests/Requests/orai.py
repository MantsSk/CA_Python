import requests
import re

text = requests.get("https://orai.15min.lt/prognozes").text
text = text[text.find("Vilnius"):]
temperature = re.findall("[\+|\-]\d\d?°", text)[0]

pass
