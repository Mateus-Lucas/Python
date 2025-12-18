print('\033[1;33m' + '=' * 20, '| Desafio 74 |', '=' * 20 + '\033[m')

''' Crie um programa que vai gerar cinco números aleatórios e colocar wm uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.'''

from random import randint

# lista = []

# # Looping que me traz 5 números aleatórios e adiconam na lista
# for _ in range(5):
#     numero = randint(0, 100)
#     lista.append(numero)

# # Transformando a lista em tupla
# tupla = tuple(lista)

# É possível ramdomizar dentro de uma tupla 
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Números sorteados:', end=' ')
for n in tupla:
    print(n, end=' ')

print(f'\nO maior valor da tupla é: {max(tupla)}')
print(f'O menor valor da tupla é: {min(tupla)}')