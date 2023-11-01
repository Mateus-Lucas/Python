# 07 - Faça um Programa que leia três números e mostre o maior e o menor deles.
# a = numero 1 
# b = numero 2
# c = numero 3

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

if a > b and a > c and b > c:
    print(f'O número {a} é o maior e {c} é o menor')

elif a > b and a > c and c > b:
    print(f'O número {a} é o maior e {b} é o menor')

elif b > a and b > c and a > c:
    print(f'O número {b} é o maior e {c} é o menor') 

elif b > a and b > c and c > a:
    print(f'O número {b} é o maior e {a} é o menor') 

elif c > a and c > b and a > b:
    print(f'O número {c} é o maior e {b} é o menor') 

elif c > a and c > b and b > a:
    print(f'O número {c} é o maior e {a} é o menor') 

else:
    print('Numeros iguais, lógica inválida')
