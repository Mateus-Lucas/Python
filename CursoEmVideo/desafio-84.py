print('\033[1;33m' + '=' * 20 + ' | Desafio 84 | ' + '=' * 20 + '\033[m')

'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.
'''

pessoas = []      # Lista principal com todas as pessoas
pessoa = []       # Lista auxiliar para nome e peso
maior = menor = 0 # Controle de maior e menor peso

while True:
    # Cadastro dos dados
    pessoa.append(input('Informe o seu nome: '))
    pessoa.append(float(input('Informe o seu peso: ')))

    # Define maior e menor peso no primeiro cadastro
    if not pessoas:
        maior = menor = pessoa[1]
    else:
        # Atualiza maior e menor peso
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

    # Salva a pessoa e limpa a lista auxiliar
    pessoas.append(pessoa[:])  # [:] garante a cópia correta
    pessoa.clear()

    # Validação de continuação
    continuar = input('Você deseja continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Digite apenas S ou N: ').strip().upper()[0]

    if continuar == 'N':
        break

# Exibição dos resultados
print('\n' + '-' * 40)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')

print(f'O maior peso foi {maior}kg. Peso de:', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi {menor}kg. Peso de:', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

print('\n' + '-' * 40)
