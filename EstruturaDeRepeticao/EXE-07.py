# 07 - Faça um programa que leia 5 números e informe o maior número.

numeros = [1, 8, 15, 12, 9]

for numero in numeros:
    print(f'número da lista: {numero}')
   
print(f'O maior número da lista é: {max(numeros, key=int)}')
