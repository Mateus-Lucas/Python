print('='*11,'| DESAFIO 17 |', '='*11)
''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre 
o comprimento da hipotenusa'''

from math import hypot

c_oposto = float(input('Informe o valor do cateto oposto: '))
c_adjacente = float(input('Informe o valor do cateto adjacente: '))

h = (hypot(c_oposto, c_adjacente))

print(f'A hipotenusa dos catetos {c_oposto} e {c_adjacente} é {h:.2f}')