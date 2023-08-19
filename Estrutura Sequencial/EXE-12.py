#12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

# Entrada de dados da variavel altura
altura = float(input('Informe sua altura em metros: '))

# Calculo para peso ideal
peso_ideal = (72.7*altura) - 58

print(f'Seu pedo ideal é aproximadamente {peso_ideal:.0f}kg')
