import math

area_pintura = float(input('Informe a área a ser pintada em metros quadrados: '))
litro_tinta = area_pintura / 6
lata_tinta = 18
galao_tinta = 3.6
quantidade_latas = 0
quantidade_galoes = 0

# Verificando se o valor é maior que zero
if area_pintura > 0:
    quantidade_latas = math.ceil(litro_tinta / lata_tinta)
    preco_latas = quantidade_latas * 80

    quantidade_galoes = math.ceil(litro_tinta / galao_tinta)
    preco_galoes = quantidade_galoes * 25

    # Mistura de latas e galões
    quantidade_latas_mistura = math.floor(litro_tinta / lata_tinta)
    litros_restantes = litro_tinta - quantidade_latas_mistura * lata_tinta
    quantidade_galoes_mistura = math.ceil(litros_restantes / galao_tinta)
    preco_mistura = (quantidade_latas_mistura * 80) + (quantidade_galoes_mistura * 25)

    print(f'Área de {area_pintura} metros quadrados')
    print(f'Você precisa comprar {litro_tinta:.2f} litros de tinta')

    print(f'\nOpção 1: Comprar apenas latas de 18 litros')
    print(f'Você pode comprar {quantidade_latas} lata(s) no valor total de R${preco_latas:.2f}')

    print(f'\nOpção 2: Comprar apenas galões de 3,6 litros')
    print(f'Você pode comprar {quantidade_galoes} galão(ões) no valor total de R${preco_galoes:.2f}')

    print(f'\nOpção 3: Misturar latas e galões para menor desperdício')
    print(f'Você pode comprar {quantidade_latas_mistura} lata(s) e {quantidade_galoes_mistura} galão(ões) no valor total de R${preco_mistura:.2f}')

else:
    print('Área inválida. A área a ser pintada deve ser maior que zero.')
