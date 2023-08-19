# 16- Faça um programa para uma loja de tintas.O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_pintura = float(input('Informe a área a ser pintada em metros quadrados: '))

litros_tinta = area_pintura/3
litros_lata = 18

# condicional para verificar se o valor é maior que zero e criando uma nova variavel inteira
if litros_tinta > 0:
    quantidade_latas = litros_tinta/litros_lata
    quantidade_latas_arredondada = int(quantidade_latas)

    # condional para transformar os valores decimais no inteiro maior mais proximo
    if quantidade_latas > quantidade_latas_arredondada:
         quantidade_latas_arredondada += 1

         preco_total = quantidade_latas_arredondada * 80 

print(f'Área de {area_pintura} metros')
print(f'Você precisa de {litros_tinta:.0f} litros de tinta')
print(f'Você precisa comprar {quantidade_latas_arredondada} latas no valor total de R${preco_total}')