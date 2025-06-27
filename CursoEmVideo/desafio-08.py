print('='*11,'| DESAFIO 08 |', '='*11)
# Escreva um programa que leia um valor em metros e o exiba convertido em centímeros e milímetros
# Mostre também a quatidade de quilômetros, hectômetros, decâmetros, decímetros

valor = float(input('Informe um valor em metros: '))

km = valor * 0.001
hm = valor * 0.01
dam = valor * 0.1
dm = valor * 10
cm = valor * 100
mm= valor * 1000

print(f'Os valores são: \n')
print(f' Km = {km}km\n Hm = {hm}hm\n Dam = {dam}dam\n Dm = {dm}dm\n Cm = {cm}cm\n Mm = {mm}mm')