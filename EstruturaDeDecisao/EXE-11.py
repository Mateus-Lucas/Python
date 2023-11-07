# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Informe o seu salário: '))

percentual_aplicado = 0
novo_salario = 0
valor_aumento = 0

if salario <= 280:
    percentual_aplicado = 0.2
elif salario <= 700:
    percentual_aplicado = 0.15
elif salario < 1500:
    percentual_aplicado = 0.1
else:
    percentual_aplicado = 0.05

novo_salario = salario + (salario * percentual_aplicado)
valor_aumento = novo_salario - salario

print(f'Salário antigo: R$ {salario:.2f}')
print(f'Percentual aplicado: {int(percentual_aplicado * 100)}%')
print(f'Valor do aumento: R$ {valor_aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')
