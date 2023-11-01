# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
# a = Valor do primeiro produto
# b = Valor do segundo produto
# c = Valor do terceiro produto

a = float(input('Informe o valor do primeiro produto: '))
b = float(input('Informe o valor do segundo produto: '))
c = float(input('Informe o valor do terceiro produto: '))

if a < b and a < c:
    print('Opte pelo primeiro produto pois é mais barato')
if b < a and b < c:
    print('Opte pelo segundo produto pois é mais barato')
if c < a and c < b:
    print('Opte pelo terceiro produto pois é mais barato')