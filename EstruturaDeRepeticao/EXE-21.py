# 21 - Faça um programa que peça um número inteiro e determine se ele é ou não um 
# número primo.Um número primo é aquele que é divisível somente por ele mesmo e por 1.

import math

numero = int(input('Informe um número inteiro: '))

# Verifica se o número é menor que 2, pois números menores que 2 não são primos
if numero < 2:
    print('Não é primo')
else:
    # Assume inicialmente que o número é primo
    is_primo = True
    
    # Loop para verificar divisibilidade do número por valores de i de 2 até a raiz quadrada do número
    for i in range(2, math.isqrt(numero) + 1):
        # Se o número for divisível por i, ele não é primo
        if numero % i == 0:
            is_primo = False
            break

    # Imprime o resultado com base na verificação
    if is_primo:
        print('É primo')
    else:
        print('Não é primo')

