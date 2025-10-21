print('=' * 20, '| Desafio 50 |' ,'=' * 20)

"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""

soma = 0

for i in range(1, 7):
    num = int(input(f'Digite o {i}º valor: ')) #Pedindo um número 6 vezes
    if num % 2 == 0:
        soma += num

print(f'\033[1;33mA soma dos números pares digitados é {soma}\033[m')
