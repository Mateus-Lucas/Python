# 14 - Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

# Iniciando váriaveis 
numeros = []
numero = 0
pares = 0
impares = 0

# Looping que acaba quando completa 10 números
while len(numeros) < 10:
    numero = int(input('Informe um número: '))
    # Função interna "append" para adicionar elementos numa lista 
    numeros.append(numero)

    # Condicional if para separar ímpares de pares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números impares: {impares}')