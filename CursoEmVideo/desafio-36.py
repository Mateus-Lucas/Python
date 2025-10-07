print('=' * 20, '| Desafio 20 |', '=' * 20)

"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em 
quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário 
ou então o empréstimo será negado.
"""

print('-=' * 28)
print(' ' * 17, '\033[1;33mEMPRÉSTIMO BANCÁRIO\033[m')
print('-=' * 28)

valor_casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos_parcela = int(input('Informe em quantos anos você vai pagar: '))

# Cálculo correto da prestação mensal
prestacao_mensal = valor_casa / (anos_parcela * 12)

# Cálculo da porcentagem da prestação em relação ao salário
porcentagem_prestacao = (prestacao_mensal / salario) * 100

print(f'\nA prestação mensal será de R${prestacao_mensal:.2f}, equivalente a {porcentagem_prestacao:.2f}% do seu salário.')

if prestacao_mensal > salario * 0.3:
    print('\033[1;31mEmpréstimo negado!\033[m')
    print(f'O valor da prestação (R${prestacao_mensal:.2f}) excede 30% do seu salário.')
else:
    print('\033[1;32mEmpréstimo aprovado! Parabéns!\033[m')
