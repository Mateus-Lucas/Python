#09 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

#definição de variaveis
graus_f = float(input('Informe a terperatura em graus Fahrenheit: '))

#calculos
graus_c = 5*((graus_f-32)/9)

#exibindo resultados
print(f'{graus_f:.1f} graus Fahrenheit equivelem a aproximadamente {graus_c:.1f} graus Celsius')