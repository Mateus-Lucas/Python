#06 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#definição de variaveis
raio = int(input('Digite o valor do raio em centimetros: '))

#calculo da area
area = 3.14*(raio**2)

#mostrando resultado da area
print(f'O valor da área em cm é aproximadamente: {area:.2f} cm²')