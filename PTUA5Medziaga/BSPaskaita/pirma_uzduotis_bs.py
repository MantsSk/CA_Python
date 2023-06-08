from bs4 import BeautifulSoup

html = '''
<html>
<body>
<h1>Sveiki atvykę į mano tinklalapį</h1>
<p>Ši yra pastraipa.</p>
</body>
</html>
'''


soup = BeautifulSoup(html, 'html.parser')

# Ieškome konkretaus elemento
pastraipa = soup.find('p')

# Išgauti ir spausdiname tekstą
tekstas = pastraipa.get_text()
print(tekstas)