print('\033[1;33m' + '=' * 20 + ' | Desafio 114 | ' + '=' * 20 + '\033[m')

''' Crie um código em Python que teste se o site Pudim está acessível pelo
computador usado.'''

import urllib.request
from urllib.error import URLError

site = 'https://www.google.com'

try:
    urllib.request.urlopen(site)
except URLError:
    print(f'Não foi possível acessar {site}')
else:
    print(f'{site} está acessível!')