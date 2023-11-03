# 09 - Faça um Programa que leia três números e mostre-os em ordem decrescente
# a = numero 1 
# b = numero 2
# c = numero 3

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

numeros = [a, b, c]

numeros_decrescente = sorted(numeros, reverse=True)

print(f'Ordem descrescente: {numeros_decrescente}')

