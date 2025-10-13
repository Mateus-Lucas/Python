print('=' * 20, '| Desafio 43 |', '=' * 20)

"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

def linha():
    print('\033[1;33m' + '-=' * 20 + '\033[m')

linha()
print('\033[1;36m{:^40}\033[m'.format('CALCULADORA DE IMC'))
linha()

peso = float(input('Qual o seu peso (kg)? '))
altura = float(input('Qual a sua altura (m)? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = 'abaixo do peso'
elif imc <= 25:
    status = 'no peso ideal'
elif imc <= 30:
    status = 'com sobrepeso'
elif imc <= 40:
    status = 'com obesidade'
else:
    status = 'com obesidade mórbida, procure um médico imediatamente!'

print()
print(f'\033[1;35mSeu IMC é {imc:.2f}\033[m e você está \033[1;33m{status}\033[m.')
