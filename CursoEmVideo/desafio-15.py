print('='*11,'| DESAFIO 15 |', '='*11)
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado 

km_rodado = int(input('Informe a quantidade de km percorridos: '))
dias_alugados = int(input('Por quantos dias ele foi alugado? '))

custo_aluguel = (km_rodado*0.15) + (dias_alugados*60)

print(f'Percorrento {km_rodado}Km durante {dias_alugados}dias o custo do aluguel fica R${custo_aluguel:.2f}')