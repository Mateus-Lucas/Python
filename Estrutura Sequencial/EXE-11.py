#11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

#definição de variaveis
num1 = int(input('Digite o valor do primeiro número: '))
num2 = int(input('Digite o valor do segundo número: '))
num3 = float(input('Digite o valor do terceiro número: '))

#calculos
condicao1 = (num1*2)*(num2/2)
condicao2 = (num1*3)+num3
condicao3 = num3**3

#exibindo resultados
print(f'O produto do dobro do primeiro com metade do segundo = {condicao1:.2f}')
print(f'A soma do triplo do primeiro com o terceiro = {condicao2:.2f}')
print(f'O terceiro elevado ao cubo = {condicao3:.2f}')

