print('\033[1;33m' + '=' * 20 + ' | Desafio 109 | ' + '=' * 20 + '\033[m')

''' Modifique as funções que foram criadas nos desafios 107 para que elas
aceitem um parâmetro a mais, informando se o valor retornado por elas
vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

import moeda

p = float(input('Informe o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 30%, temos {moeda.diminuir(p, 30, True)}')