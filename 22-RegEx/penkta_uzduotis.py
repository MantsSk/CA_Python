import re

file = open('most_visited.html', 'r')
html = file.read()
domain_regex = re.compile(r'\w+\.\w+\.?\w*')
extracted_domains = domain_regex.findall(html)
print(extracted_domains)