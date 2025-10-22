print('=' * 20, '| Desafio 51 |', '=' * 20)

'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

def linha():  # Função de estilização de linha
    print('\033[1;33m=' * 40, '\033[m') 

linha()
print(' ' * 10, '10 Termos de uma PA')  # Título
linha()

p1 = int(input('Digite o primeiro termo: '))  # Primeiro termo
r = int(input('Digite a razão: '))  # Razão da PA

for i in range(1, 11):  # Exibir os 10 primeiros termos
    termo = p1 + (i - 1) * r
    print(f'{i}° termo: {termo}')
