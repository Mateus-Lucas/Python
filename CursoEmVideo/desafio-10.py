print('='*11,'| DESAFIO 10 |', '='*11)
# Crie um programa  que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares e euros ela pode comprar
# Considere US$ 1,00 = R$ 5,47
# Considere €1,00 = R$ 6,42

saldo = float(input('Informe seu saldo em reais: R$'))
saldo_dolar = saldo/5.47
saldo_euro = saldo/6.42

print(f'Com R${saldo:.2f} você pode comprar US${saldo_dolar:.2f} e €{saldo_euro:.2f}')
