print('=' * 20, '| Desafio 44 |' ,'=' * 20)

'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto 
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

def linha():
    print('\033[1;34m' + '-=-' * 15 + '\033[m')

linha()
print(f'{"LOJAS AMERICANAS":^50}')
linha()

preco = float(input('Informe o valor do produto: R$'))
pagamento = int(input(
    '\nInforme a forma de pagamento:\n'
    '[ 1 ] - Dinheiro\n'
    '[ 2 ] - Cheque\n'
    '[ 3 ] - Cartão de Crédito\n> '
))

if pagamento in [1, 2, 3]:
    if pagamento in [1, 2]:
        print('\033[1;32mPagamento à vista: 10% de desconto!\033[m')
        preco -= preco * 0.10
    else:
        parcelas = int(input('Número de parcelas: '))
        if parcelas < 1:
            print('\033[1;31mNúmero de parcelas inválido!\033[m')
        elif parcelas == 1:
            print('\033[1;32mÀ vista no cartão: 5% de desconto!\033[m')
            preco -= preco * 0.05
        elif parcelas == 2:
            print(f'\033[1;33mEm 2x no cartão: preço normal ({parcelas}x de R${preco/parcelas:.2f})\033[m')
        else:
            preco += preco * 0.20
            print(f'\033[1;31mEm {parcelas}x no cartão: 20% de juros ({parcelas}x de R${preco/parcelas:.2f})\033[m')
else:
    print('\033[1;31mForma de pagamento inválida!\033[m')

print(f'\n\033[1mValor final a pagar: R${preco:.2f}\033[m')
