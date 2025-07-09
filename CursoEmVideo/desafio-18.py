print('='*11,'| DESAFIO 18 |', '='*11)
''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''

from math import cos, sin, tan, radians

angulo = float(input('Informe um valor para o ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f' O seno de {angulo}° é {seno:.2f}\n o cosseno é {cosseno:.2f}\n e a tangente é {tangente:.2f}')

