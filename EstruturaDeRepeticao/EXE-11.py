# 11 - Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
numero = 0
soma = 0

for numero in range(num1, num2 + 1):
    soma += numero
 
print(f'A soma dos números é: {soma}')


