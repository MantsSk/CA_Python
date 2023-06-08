import requests

def sites_headers_data(*args):
    print('URL\t\t\tServer')
    print('-------------------------------------')
    for site in args:
        r = requests.get(site)
        result = r.headers
        print(f'{r.url}\t{result["Server"]}')

sites_headers_data('http://delfi.lt', 'http://alfa.lt', 'http://15min.lt', 'http://lrytas.lt', 'http://google.com')