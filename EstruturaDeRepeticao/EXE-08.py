# 08 - Faça um programa que leia 5 números e informe a soma e a média dos números

import numpy as np

numeros = np.random.randint(1, 100, 5)
quantidade = len(numeros)

soma = sum(numeros)
media = soma / quantidade

print('Números:', end=' ')
for numero in numeros:
    print(numero, end=' ')

print(f'\nSoma: {soma}')
print(f'Média: {media}')