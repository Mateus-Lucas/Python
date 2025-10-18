print('=' * 20, '| Desafio 46 |' ,'=' * 20)

'''
 Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
 indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

import time 

def linha():
    print('-=' * 20)

linha()
print(' ' * 10, '\033[1;33mCONTAGEM REGRESSIVA\033[m')
linha()

for i in range(10, -1, -1):  # agora inclui o 0
    print(f'\033[1;36m{i}\033[m')
    time.sleep(1)

print('\033[1;32m🎆 FELIZ ANO NOVO!!! 🎇\033[m')
