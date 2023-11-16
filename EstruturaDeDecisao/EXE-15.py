# 15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
# lado 1 = a
# lado 2 = b
# lado 3 = c

a = int(input('Informe o primeiro lado do triângulo: '))
b = int(input('Informe o segundo lado do triângulo: '))
c = int(input('Informe o terceiro lado do triângulo: '))

triangulo = ''

if  a < b + c and  b < a + c and  c < a + b:
    if a == b and b == c:
        triangulo = 'Equilátero'
    elif a == b or a == c or b == c:
        triangulo = 'Isósceles'
    else: 
        triangulo = 'Escaleno'
    print(f'O triângulo é {triangulo}')  
else:
    print('Não é um triângulo')
    