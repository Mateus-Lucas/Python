print('='*11,'| DESAFIO 13 |', '='*11)
# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumennto.

salario = float(input('Qual é o valor do seu salário? R$'))

salario_ajustado = salario+(salario*0.15)

print(f'O seu salário antigo é R${salario:.2f} e o seu novo salário com 15% de aumento é R${salario_ajustado:.2f}')