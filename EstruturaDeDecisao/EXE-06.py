# 06 - Faça um Programa que leia três números e mostre o maior deles.
# a = numero 1 
# b = numero 2
# c = numero 3

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

if a > b and a > c:
    print(f'O número {a} é o maior')

elif b > a and b > c:
    print(f'O número {b} é o maior')

elif c > a and c > b:
    print(f'O número {c} é o maior') 

else:
    print('Numeros maiores iguais')
