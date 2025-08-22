print('=' * 11, '| DESAFIO 25 |', '=' * 11)

"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = str(input('Informe o seu nome completo: ')).strip()

print(f'Seu nome tem silva?: {'SILVA' in nome.upper()}')
