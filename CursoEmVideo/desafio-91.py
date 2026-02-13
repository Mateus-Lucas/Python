print('\033[1;33m' + '=' * 20 + ' | Desafio 91 | ' + '=' * 20 + '\033[m')

''' Crie um programa onde 4 jogadores joguem com um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''

from random import randint
from time import sleep

# Declando dicionário já com valores sorteados
jogo = {
    'jogador1': randint(1, 6), 
    'jogador2': randint(1, 6), 
    'jogador3': randint(1, 6), 
    'jogador4': randint(1, 6)
}

# Looping para exbir os jogadores e seus respectivos dados
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado.')
print('-=' * 30)

# Ranqueando os jogadores de acordo com o número dos dados
print(' == RANKING DOS JOGADORES == ')
jogo_ordenado = sorted(jogo.items(), key=lambda x: x[1], reverse=True)
cont = 1
for k, v in jogo_ordenado:
    sleep(1)
    print(f'  {cont}° lugar: {k} com {v}')
    cont += 1


#    CÓDIGO GUANARABA
# from operator import itemgetter

# ranking = []
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print(' == RANKING DOS JOGADORES == ')
# for i, v in enumerate(ranking):
#     print(f'   {i+1}° lugar: {v[0]} com {v[1]}')
#     sleep(1)