print('\033[1;33m' + '=' * 20 + ' | Desafio 112| ' + '=' * 20 + '\033[m')

''' Dentro do pacote utilidadeCev que criamos no desafio 111, temos um múdulos
chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar
como a função input(), mas com uma validação de dados para aceitar apenas
valores que sejam monetários.'''

from utilidadecev import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
