print('\033[1;33m' + '=' * 20 + ' | Desafio 99 | ' + '=' * 20 + '\033[m')

''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep

def maior(*numeros):
    print('-=' * 30)
    print('Analisando os valores passados...')

    # Exibindo todos os parâmetros pausadamente
    for n in numeros:
        print(n, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(numeros)} valores ao todo.')

    # Condição que exibe os valores que não vazios
    if len(numeros) != 0:
        print(f'O maior valor foi {max(numeros)}.')
    else:
        print('Nenhum valor foi informado.')

## CÓDIGO GUANABARA
# def maior(* núm):
#     cont = maior = 0
#     print('-=' * 30)
#     print('Analisando os valores passados...')
#     for valor in núm:
#         print(f'{valor} ', end='', flush=True)
#         sleep(0.3)
#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
#         cont += 1
#     print(f'Foram informador {cont} valores ao todo.')
#     print(f'O maior valor informado foi {maior}')


# PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


