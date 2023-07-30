#10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

#definição de variaveis
graus_c = float(input('Informe a terperatura em graus Celsius: '))

#calculos
graus_f = (graus_c * 1.8) + 32

#exibindo resultados
print(f'{graus_c:.1f} graus Celsius equivelem a aproximadamente {graus_f:.1f} graus Fahrenheit')