print('=' * 20, '| Desafio 52 |', '=' * 20)

"""
Faça um programa que leia um número inteiro e diga se ele é ou não número primo.
"""

def linha():
    print('\033[1;33m=\033[m' * 40)

linha()
print(' ' * 5, '\033[1;33mVERIFICADOR DE NÚMERO PRIMO\033[m')
linha()

n = int(input('Digite um número: '))
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(f'\033[1;34m{i}\033[m', end=' ')
        total += 1
    else:
        print(f'\033[1;31m{i}\033[m', end=' ')

print(f'\n\nO número \033[1;36m{n}\033[m foi divisível {total} vezes.')

if total == 2:
    print('\033[1;32mPortanto, ele é um número PRIMO!\033[m')
else:
    print('\033[1;31mPortanto, ele NÃO é um número primo.\033[m')
