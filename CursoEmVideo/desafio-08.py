print('='*11,'| DESAFIO 08 |', '='*11)
# Escreva um programa que leia um valor em metros e o exiba convertido em centímeros e milímetros

valor = int(input('Informe um valor em metros: '))

centimetros = valor * 100
milimetros = valor * 1000

print(f'{valor} metros em centímetros é {centimetros}cm e em milímetros é {milimetros}mm')