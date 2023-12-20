# 04 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
# de crescimento de 3%  e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
# A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Definimos como ano zero inical
ano = 0

populacao_a = 80000
taxa_crescimento_a = 0.03

populacao_b = 200000
taxa_crescimento_b = 0.015

# estrutura para somar um ano enquanto a população A for menor
while populacao_a < populacao_b:
    ano += 1
    populacao_a = populacao_a + (populacao_a * taxa_crescimento_a)
    populacao_b = populacao_b + (populacao_b * taxa_crescimento_b)

print(f'Levará {ano} anos para a população do país A ultrapassar ou igualar a população do país B.')
print(f'População A = {int(populacao_a)}')
print(f'População B = {int(populacao_b)}')
    