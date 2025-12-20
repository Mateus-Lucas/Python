print('\033[1;33m' + '=' * 20, '| Desafio 75 |', '=' * 20 + '\033[m')

'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.
'''

# Leitura direta dos valores em uma tupla
num = tuple(int(input(f'Digite o {i+1}º número: ')) for i in range(4))

print(f'\nVocê digitou os valores {num}')

# Quantidade de vezes que aparece o número 9
print(f'O valor 9 apareceu {num.count(9)} vez(es)')

# Primeira posição do número 3 (se existir)
if 3 in num:
    print(f'O valor 3 apareceu pela primeira vez na posição {num.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')

# Números pares
print('Os valores pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
