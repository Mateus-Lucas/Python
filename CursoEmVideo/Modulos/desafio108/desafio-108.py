print('\033[1;33m' + '=' * 20 + ' | Desafio 108 | ' + '=' * 20 + '\033[m')

''' Adapte o código do desafio 107, criando uma função adicional chamada
moeda() que consiga mostrar os valores com um valor monetário formatado'''

from desafio108 import moeda

p = float(input('Informe o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')