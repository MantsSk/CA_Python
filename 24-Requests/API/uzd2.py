import requests
import webbrowser as wb

url = 'http://www.recipepuppy.com/api/'

def get_recipes(query):
    payload = {'q': query}
    r = requests.get(f'{url}', params=payload)
    response = r.json()
    for recipe in response['results']:
        with open(f'{query}.html', 'a') as html:
            html.write(f'''
<a href="{recipe['href']}">{recipe['title']}</a></br>
<img src="{recipe['thumbnail']}"></br></br>
            ''')
    wb.open_new_tab(f'{query}.html')
    # os.remove(f'{query}.html')

get_recipes('salmon')
