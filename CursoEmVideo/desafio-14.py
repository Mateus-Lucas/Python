print('='*11,'| DESAFIO 14 |', '='*11)
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F e K

c = int(input('Informe a temperaruta em °C: '))

f = (c*1.8) + 32
k = c+273

print(f"{c}°C equivalem a {f}°F  e a {k} kelvin")

