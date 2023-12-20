# 05 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

repetir = 'sim'

while repetir == 'sim':
    ano = 0

    populacao_a = int(input('Informe a População do país A: '))
    taxa_crescimento_a = float(input('Informe a taxa de crescimento em porcentagem: '))

    populacao_b = int(input('Informe a População do país B: '))
    taxa_crescimento_b = float(input('Informe a taxa de crescimento em porcentagem: '))

    # Atualizando entrada para porcentagem 
    taxa_crescimento_a = taxa_crescimento_a / 100
    taxa_crescimento_b = taxa_crescimento_b / 100

    # Condicional que não deixa o sistema continuar em looping
    if taxa_crescimento_a > taxa_crescimento_b:
        # estrutura para somar um ano enquanto a população A for menor
        while populacao_a < populacao_b:
            ano += 1
            populacao_a = populacao_a + (populacao_a * taxa_crescimento_a)
            populacao_b = populacao_b + (populacao_b * taxa_crescimento_b)

        print(f'Levará {ano} anos para a população do país A ultrapassar ou igualar a população do país B.')
        print(f'População A = {int(populacao_a)}')
        print(f'População B = {int(populacao_b)}')

    else: 
        print('A taxa de crescimento do país B não pode ser maior ou igual que a de A')

    repetir = input('Deseja repetir, sim ou não? ').lower()

