#08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

#definição de variaveis
ganho_hora = float(input('Digite o valor que você ganha por hora: '))
hora_mes = int(input('Digite quantas horas você trabalha por mês: '))

#calculos
salario = (ganho_hora*hora_mes)

#exibindo resultados
print(f'Você ganha {salario:.2f} reais por mês')

