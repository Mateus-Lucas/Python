# 06 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

numero = 0

for numero in range(1, 21):
    print(numero)

for numero in range(1, 21):
    print(numero, end=" ")