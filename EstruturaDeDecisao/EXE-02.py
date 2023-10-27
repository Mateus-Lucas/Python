# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input('Informe um valor: '))

if valor > 0:
    print(f'O numero {valor} é positivo')
elif valor < 0:
    print(f'O numero {valor} é negativo')
else: 
    print('O valor é zero')