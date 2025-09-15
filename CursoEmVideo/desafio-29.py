print('=' * 11, '| Desafio 29 |' ,'=' * 11)

"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = float(input('Informe a velocidade do carro em Km/h: '))
print('-=-' * 20)

if velocidade > 80:
    km_ultrapassado = velocidade - 80
    valor_multa = km_ultrapassado * 7
    print('VOCê FOI MULTADO! Ande mais devagar.')
    print('-=-' * 20)
    print(f'Sua multa ficou no valor de R${valor_multa:.2f}')
else:
    print('Parabéns, Sua velocidade éstá dentro do limite!')
print('-=-' * 20)
print('Tenha um bom dia! Dirija com segurança!')