print('\033[1;33m' + '=' * 20 + ' | Desafio 107 | ' + '=' * 20 + '\033[m')

''' Crie um módulo chamado moeda.py que tenhas as funções incorporadas
aumentar(), diminuir(), dobro() e metade(). Faça também um programa que
importe esse módulo e use algumas dessas funções'''

import moeda

p = float(input('Informe o preço: R$'))

print(moeda.aumentar(p, 10))
print(moeda.diminuir(p, 15))
print(moeda.dobro(p))
print(moeda.metade(p))