print('\033[1;33m' + '=' * 20, '| Desafio 79 |', '=' * 20 + '\033[m')

'''
Crie um programa onde o usuário pode digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

numeros = []

# Adicionando valores à lista
while True:
    num = int(input('Adicione um valor à lista: '))

    # Condicional que impede números repetidos
    if num not in numeros:
        numeros.append(num)
    else:
        print('Insira apenas valores que não estão na lista.')

    continuar = input('Você quer continuar? [S/N]: ').strip().upper()[0]

    # Validação da resposta do usuário
    while continuar not in 'SN':
        continuar = input('Por favor, digite apenas S para sim ou N para não: ').strip().upper()[0]

    # Encerra o programa se o usuário digitar "N"
    if continuar == 'N':
        break

# Ordenando a lista
numeros.sort()

print(f'Os números únicos digitados em ordem crescente são: {numeros}')
