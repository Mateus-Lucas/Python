print('=' * 20, '| Desafio 59 |' ,'=' * 20)

''' 
Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:     
Seu programa deverá realizar a operação solicitada em cada caso.                         
[1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa 
'''
from time import sleep
import os

# Limpa a tela no início (funciona no Windows e Linux)
os.system('cls' if os.name == 'nt' else 'clear')

print('\033[1;32m' + '=' * 50)
print(' ' * 10 + '| 🧮 Desafio 59 — Calculadora |')
print('=' * 50 + '\033[m')
sleep(0.8)

print('\033[1;36mBem-vindo à calculadora interativa!\033[m')
print('-' * 50)

n1 = int(input('\033[1;33mInforme o primeiro valor:\033[m '))
n2 = int(input('\033[1;33mInforme o segundo valor:\033[m '))

while True:
    print('\n' + '\033[1;34m' + '-' * 50 + '\033[m')
    print('\033[1;35mEscolha uma das opções abaixo:\033[m')
    print('\033[1;32m[1]\033[m Somar')
    print('\033[1;32m[2]\033[m Multiplicar')
    print('\033[1;32m[3]\033[m Mostrar o maior')
    print('\033[1;32m[4]\033[m Inserir novos números')
    print('\033[1;31m[5]\033[m Sair do programa')
    print('\033[1;34m' + '-' * 50 + '\033[m')

    try:
        opcao = int(input('\033[1;33mDigite sua opção: \033[m'))
    except ValueError:
        print('\033[1;31mEntrada inválida! Digite apenas números.\033[m')
        continue

    if opcao == 1:
        print(f'\033[1;36mResultado:\033[m {n1} + {n2} = \033[1;32m{n1 + n2}\033[m')
    elif opcao == 2:
        print(f'\033[1;36mResultado:\033[m {n1} x {n2} = \033[1;32m{n1 * n2}\033[m')
    elif opcao == 3:
        maior = n1 if n1 > n2 else n2
        print(f'\033[1;36mResultado:\033[m O maior número entre {n1} e {n2} é \033[1;32m{maior}\033[m')
    elif opcao == 4:
        print('\033[1;34mVamos inserir novos valores...\033[m')
        sleep(0.5)
        n1 = int(input('\033[1;33mInforme o primeiro valor:\033[m '))
        n2 = int(input('\033[1;33mInforme o segundo valor:\033[m '))
    elif opcao == 5:
        print('\n\033[1;32mEncerrando a calculadora...\033[m')
        sleep(1)
        print('\033[1;35mObrigado por utilizar o programa! 👋\033[m')
        print('\033[1;34mFeito por: Mateus Lucas 💻\033[m')
        print('=' * 50)
        break
    else:
        print('\033[1;31mOpção inválida! Tente novamente.\033[m')

    sleep(1.2)
