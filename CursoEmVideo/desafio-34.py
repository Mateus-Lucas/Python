print('=' * 11,'| Desafio 34 |','=' * 11)

'''
 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1.250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%
'''

salario_atual = float(input('Por favor! Informe o seu salário: R$'))
reajuste = 0

#Define a porcentagem de aumento
if salario_atual > 1250:
    percentual_aumento = 10
else:
    percentual_aumento = 15

#Calcula o valor do aumento e o novo salário
valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

#Exibe o resultado de forma clara

print(f'Salário antigo: R${salario_atual:.2f}')
print(f'Aumento de {percentual_aumento}%: R${valor_aumento:.2f}')
print(f'Novo salário: R%{novo_salario:.2f}')
