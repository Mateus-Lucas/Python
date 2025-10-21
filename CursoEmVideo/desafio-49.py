print('=' * 20, '| Desafio 49 |', '=' * 20)

'''
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que utilizando o laço for.
'''

n = int(input('Digite um número para ver sua tabuada: '))

print('-=' * 10)
print(f'\033[1;33mTABUADA DO {n}\033[m')
print('-=' * 10)

for i in range(1, 11):
    print(f'\033[1;36m{i}\033[m x \033[1;33m{n}\033[m = \033[1;32m{i * n}\033[m')

print('-=' * 10)
