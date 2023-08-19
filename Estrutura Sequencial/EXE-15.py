# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%) : R$ = Salário Liquido : R$

ganho_hora = float(input('Informe quanto você ganha por hora: '))
horas_mes = int(input('Informe quantas horas você trabalha no mês: '))

salario_bruto = ganho_hora*horas_mes
imposto = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - (imposto + inss + sindicato)

print(f'Seu salário bruto é de R${salario_bruto:.2f}')
print(f'Você paga R${imposto:.2f} de impostos')
print(f'Você paga R${inss:.2f} do inss')
print(f'Você paga R${sindicato:.2f} do sindicato')
print(f'Portanto seu sálario liquido é de R${salario_liquido:.2f}')

