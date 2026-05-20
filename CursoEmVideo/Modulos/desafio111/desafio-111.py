print('\033[1;33m' + '=' * 20 + ' | Desafio 111| ' + '=' * 20 + '\033[m')

''' Crie um pacote chamado utilidadescev que tenha dois módulos internos
chamados moeda e dado. Transfira todas as funções utilizadas nos desafios
107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.'''

from utilidadecev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)
