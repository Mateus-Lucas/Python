# 10 - Faça um programa que receba dois números inteiros e 
# gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))


for numero in range(num1, num2 + 1):
    print(numero)