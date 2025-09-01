print('=' * 11, '| DESAFIO 27 |', '=' * 11)

"""
  Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
  Ex: Ana Maria de Souza
  primeiro: Ana
  último: Souza
"""

nome = str(input('Informe seu nome completo: ')).strip()

nome = nome.split()
print(f'O primeiro nome é {nome[0]}')
print(f'O último nome é {nome[-1]}')

# CÓDIGO INICIAL
# quant_nomes = nome.split()
# quant_nomes = quant_nomes.count([])

# print(f'O primeiro nome é {nome.split()[0]}')
# print(f'O último nome é {nome.split()[quant_nomes - 1]}')