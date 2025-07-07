print('='*11,'| DESAFIO 16 |', '='*11)
# Crie um programa que leia um número Real qualquer e mostre na tela sua porção inteira

from math import floor

num = float(input('Informe um número Real: '))
inteiro = floor(num)

print(f'A porção inteira do número {num} é {inteiro}')