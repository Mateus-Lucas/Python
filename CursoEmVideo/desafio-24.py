print('=' * 11, '| DESAFIO 24 |', '=' * 11)

"""
Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "SANTO""
"""

cidade = str(input('Em que cidade vocÊ nasceu? ')).strip()

print(cidade[:5].upper() == 'SANTO')