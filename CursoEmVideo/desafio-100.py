print('\033[1;33m' + '=' * 20 + ' | Desafio 100 | ' + '=' * 20 + '\033[m')

''' Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colacá-los dentro da lista e a segunda função vai mostrar 
a soma entre todos os valores PARES sorteados pela função anterior'''

from random import randint
from time import sleep

# numeros = []

# # Funçaõ que sorteia 5 valores
# def sorteia():
#     for c in range(5):
#         numeros.append(randint(1, 10))
#     print('Sorteando 5 valores da lista: ')
#     for n in numeros:
#         print(f'{n}', end=' ', flush=True)  
#         sleep(0.3)
#     print('PRONTO!')


# # Função que soma os valores pares da lista
# def somaPar(numeros):
#     soma = 0
#     for n in numeros:
#         if n % 2 == 0:
#             soma += n
#     print(f'Somando os valores pares de {numeros}, temos {soma}')

# # PROGRAMA PRINCIPAL
# sorteia()
# somaPar(numeros)


# CÓDIGO GUANABARA
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {lista}, temos {soma}')


números = list()
sorteia(números)
somaPar(números)