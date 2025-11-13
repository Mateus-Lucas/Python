print('=' * 20, '| Desafio 63 |', '=' * 20)

'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8...
'''

from time import sleep

print('\033[1;33m' + '=' * 20, '| Desafio 63 |', '=' * 20 + '\033[m')

print('''
\033[1;36mSequência de Fibonacci\033[m
Mostrando os primeiros termos conforme solicitado.
''')

n = int(input('\033[1;32mQuantos termos deseja mostrar?\033[m '))

# t1 = termo antigo | t2 = termo atual | t3 = novo termo | contador
t1 = 0
t2 = 1
c = 0

print('\n\033[1;35mGerando sequência...\033[m')
sleep(0.8)

print('\033[1;34m' + '-' * 50 + '\033[m')
print(f'\033[1;33m{n} termos Fibonacci:\033[m ', end='')
print(f'\033[1;32m{t1} -> {t2}\033[m', end='')
print('\033[1;34m', end='')

c = 2  # já mostramos 2 termos

while c < n:
    sleep(0.2)
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1

print(' -> \033[1;31mFIM\033[m')
print('\033[1;34m' + '-' * 50 + '\033[m')
