# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do 
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
#  menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas 
#  trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o 
# exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

horas_mes = int(input('informe a quantidade de horas trabalhadas no mês: '))
valor_hora = float(input(('informe o valor da hora trabalhada: ')))

salario_bruto = horas_mes * valor_hora
inss = salario_bruto * 0.10
imposto = 0

if salario_bruto <= 900:
   imposto = 0
elif salario_bruto <= 1500:
   imposto = 0.05
elif salario_bruto <= 2500:
   imposto = 0.10
else:
   imposto = 0.20 

imposto_renda = salario_bruto * imposto
total_descontos = inss + imposto_renda
salario_liquido = salario_bruto - total_descontos

print(f'Salário bruto: R$ {salario_bruto:.2f}')
print(f'Imposto de renda ({imposto*100:.0f}%): R$ {imposto_renda:.2f}')
print(f'INSS (10%): R$ {inss:.2f}')
print(f'Total de descontos: R$ {total_descontos:.2f}')
print(f'Salário liquido: R$ {salario_liquido:.2f}')


