print('=' * 20, '| Desafio 64 |' ,'=' * 20)

'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar 999.
Mostre quantos números foram digitados e qual a soma deles.
'''

# c = contador | n = número individual
n = 0
numeros = []
c = 0

print('Digite valores. Para parar, digite 999.\n')

while n != 999:
    n = int(input('Informe um valor: '))
    if n != 999:
        numeros.append(n)
        c += 1

print('\n--- FIM DO LOOPING ---')

soma = sum(numeros)

print(f'Foram digitados {c} números.')
print(f'A soma deles é {soma}.')
