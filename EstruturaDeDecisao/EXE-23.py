# 23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

numero = float(input('Digite um número: '))

numero_arredondado = round(numero, 0)

if numero == numero_arredondado:
    print('Número Inteiro')
else:
    print('Número Decimal')