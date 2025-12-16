print('\033[1;33m' + '=' * 20, '| Desafio 68 |', '=' * 20 + '\033[m')

''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

from time import sleep

def linha():
    print('=' * 50)

linha()
print(' ' * 16, 'CAIXA ELETRÔNICO')
linha()

saque = int(input('Informe o valor a ser sacado: R$ '))
print('PROCESSANDO...')
sleep(1)

notas_cinquenta = saque // 50
resto = saque % 50

notas_vinte = resto // 20
resto = resto % 20

notas_dez = resto // 10
resto = resto % 10

notas_um = resto

if notas_cinquenta > 0:
    print(f'Total de {notas_cinquenta} de R$ 50')
if notas_vinte > 0:
    print(f'Total de {notas_vinte} de R$ 20')
if notas_dez > 0:
    print(f'Total de {notas_dez} de R$ 10')
if notas_um > 0:
    print(f'Total de {notas_um} de R$ 1')

linha()
print('Volte Sempre!')
