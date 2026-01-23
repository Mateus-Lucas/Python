print('\033[1;33m' + '=' * 20 + ' | Desafio 85 | ' + '=' * 20 + '\033[m')

'''
Crie um programa onde o usuário possa digitar sete
valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''

# Lista composta:
# numeros[0] -> valores pares
# numeros[1] -> valores ímpares
numeros = [[], []]

# Leitura dos 7 valores
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))

    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

# Ordenando as listas
numeros[0].sort()
numeros[1].sort()

# Exibição dos resultados
print('\n' + '-' * 40)
print(f'Valores pares em ordem crescente: {numeros[0]}')
print(f'Valores ímpares em ordem crescente: {numeros[1]}')
print('-' * 40)
