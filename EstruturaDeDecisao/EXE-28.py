# 28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade
# de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

carne = input('Você deseja compra File Duplo, Alcatra ou Picanha? ')
quantidade_kilo = float(input('Quantos quilos você quer? '))
preco_kilo = 0
valor_pagar = 0
valor_total = 0

if carne in ['Alcatra', 'Picanha', 'File Duplo']:
    if quantidade_kilo <= 5:
        if carne == 'Alcatra':
            preco_kilo = 5.9
        elif carne == 'Picanha':
            preco_kilo = 6.9
        else:
            preco_kilo = 4.9
    else:
        if carne == 'Alcatra':
            preco_kilo = 6.8
        elif carne == 'Picanha':
            preco_kilo = 7.8
        else:
            preco_kilo = 5.8

    valor_total = preco_kilo * quantidade_kilo
  
else:
  print('Carne inválida')
    

tipo_pagamento = input(f'Qual o tipo de pagamento para o valor de R${valor_total:.2f}? ')

if tipo_pagamento == 'cartão tabajara':
        desconto = 0.95
else: 
    desconto = 1

valor_pagar = valor_total * desconto

print('\n-------| Nota Fiscal |-------')
print(f'Carne secionada: {carne}')
print(f'Preço total: R${valor_total:.2f}')
print(f'Tipo de pagamento: {tipo_pagamento}')
print(f'Desconto: {(1 - desconto)*100:.0f}%')
print(f'Valor a pagar: R${valor_pagar:.2f}')





