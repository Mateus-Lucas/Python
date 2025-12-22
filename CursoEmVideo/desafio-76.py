print('\033[1;33m' + '=' * 20, '| Desafio 75 |', '=' * 20 + '\033[m')

''' Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços. organizando os dados em forma tabular'''

print('\033[1;33m' + '=' * 40 + '\033[m')
print(f'\033[1;33m{"LISTAGEM DE PREÇOS":^40}\033[m')
print('\033[1;33m' + '=' * 40 + '\033[m')

produtos = (
    'Picanha', 40.99,
    'Alcatra', 38.99,
    'Maminha', 35.99,
    'Fraudinha', 31.99,
    'Linguiça', 18.99
)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:.<30}R$ {preco:>7.2f}')

print('\033[1;33m' + '=' * 40 + '\033[m')
