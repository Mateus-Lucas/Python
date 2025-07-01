print('='*11,'| DESAFIO 12 |', '='*11)
# Faça um algoritimo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Informe o valor do produto: R$'))

print(f'O valor do produto é R${produto:.2f} e com desconto de 5% fica R${produto*0.95:.2f}')