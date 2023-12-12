# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda 
# um desconto de 10% sobre este total.
#  Escreva um algoritmo 

# Entrada do kilo das frutas
morangos = float(input('Quantos kilos de morango deseja comprar? '))
macas = float(input('Quantos kilos de maçã deseja comprar? '))

# Preço das frutas sem desconto
preco_morango = 2.5 * morangos
preco_macas = 1.8 * macas

# Condicional para verificar se morangos ou maçãs ganhas desconto
if morangos > 5:
    preco_morango = 2.2 * morangos

if macas > 5:
    preco_macas = 1.5 * macas

total_pagar = preco_macas + preco_morango

# Condicional para aplicas desconto para comprar maior que 8 kilos ou 25 reias
if morangos + macas > 8 or total_pagar > 25:
   total_pagar = total_pagar * 0.9

print(f'Quantidade de morangos (KG)= {morangos}')
print(f'Quantidade de maçãs (KG)= {macas}')
print(f'Total a pagar = R$ {total_pagar:.2f}')
