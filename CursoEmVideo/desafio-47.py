print('=' * 20, '| Desafio 47 |', '=' * 20)

'''
Crie um programa que mostre na tela todos os números pares
que estão no intervalo de 1 a 50
'''

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
