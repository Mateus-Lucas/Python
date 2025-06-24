print('='*11,'| DESAFIO 10 |', '='*11)
# Crie um programa  que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$ 1,00 = R$ 3,27

saldo = float(input('Informe seu saldo em reais: '))
saldo_dolar = saldo/3.27

print(f'O seu saudo em dólar é: US${saldo_dolar:.2f}')
