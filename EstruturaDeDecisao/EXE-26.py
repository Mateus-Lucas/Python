# 26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
#  o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 
# o preço do litro do álcool é R$ 1,90.

combustivel = input('Qual combustível deseja colocar? \n A-álcool \n G-gasolina \n')
litros = float(input('Quantos litros de combustível deseja colocar? '))

alcool = 1.90
gasolina = 2.5

if combustivel == 'A':
    if litros <= 20:
        porcentagem = 0.97
        desconto = (alcool * litros) * porcentagem
    else:
        porcentagem = 0.95
        desconto = (alcool * litros) * porcentagem
elif combustivel == 'G':
    if litros <= 20:
        porcentagem = 0.96
        desconto = (gasolina * litros) * porcentagem
    else:
        porcentagem = 0.94
        desconto = (gasolina * litros) * porcentagem
else:
    print('Combustível inválido')
    exit()

valor_desconto = (1 - porcentagem) * 100

print(f'Combustível escolhido = {combustivel}')
print(f'Litros = {litros}')
print(f'Desconto = {valor_desconto:.0f}%')
print(f'Valor sem desconto = R$ {alcool * litros:.2f}' if combustivel == 'A' else f'Valor sem desconto = R$ {gasolina * litros:.2f}')
print(f'Valor Final = R$ {desconto:.2f}')



