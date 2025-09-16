print('=' * 11, '| DESAFIO 30 |' ,'=' * 11)

'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
'''

n = int(input('Informe um número inteiro: '))
print('-=-' * 20)

if n % 2 == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é ímpar')