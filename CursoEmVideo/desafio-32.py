print('=' * 11, '| Desafio 32 |', '=' * 11)

'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''

from datetime import date

ano = int(input('Informe um ano qualquer: (caso queira ver o ano anual digite 0) '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é bissexto')
        else:
            print(f'O ano {ano} não é bissexto')  
    else:
        print(f'O ano {ano} é bissexto')  
else:
    print(f'O ano {ano} não é bissexto')
