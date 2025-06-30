print('='*11,'| DESAFIO 11 |', '='*11)
# Faça um programa que leia a largura e altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))

area = largura*altura
tinta_necessaria = area/2

print(f'A área da parede é {area}m²\ne para pintar essa área são necessários {tinta_necessaria}l de tinta')