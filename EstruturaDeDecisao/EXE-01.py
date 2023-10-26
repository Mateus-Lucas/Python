# 1 - Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input('Informe o valor do número 1: '))
num2 = int(input('Informe o valor do número 2: '))

if num1 < num2: 
    print(f'O maior valor é {num2}')

elif num2 < num1: 
    print(f'O maior valor é {num1}')

else: 
    print('Os valores são iguais')