print('\033[1;33m' + '=' * 20 + ' | Desafio 110 | ' + '=' * 20 + '\033[m')

''' Adicione ao módulo moeda.py criado nos desafios anteriores, uma função 
chamada resumo(), que mostre na tela algumas informações geradas pelas 
funções que já temos no módulo criado até aqui.'''

import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)