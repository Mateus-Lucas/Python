print('\033[1;33m' + '=' * 20, '| Desafio 68 |', '=' * 20 + '\033[m')

'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.
c) Qual é o mais barato.
'''

def linha():
    print(50 * '-')

produtos = []
precos = []
total = 0
mais_de_mil = 0 

while True:
    
    nome = str(input('Informe o nome do produto: '))
    linha()
    preco = float(input('Digite o preço desse produto: R$'))
    linha()

    # Soma total
    total += preco

    # Conta produtos acima de 1000
    if preco > 1000:
        mais_de_mil += 1

    # Guarda nome e preço
    produtos.append(nome)
    precos.append(preco)
    
    # Validação S ou N
    while True:
        continuar = str(input('Você deseja continuar? Digite "S" para sim e "N" para não: ')).upper().strip()
        linha()
        if continuar == "S" or continuar == "N":
            break
        else:
            print('Por favor digite apenas S ou N')
            linha()

    if continuar == "N":
        break

# >>> ADICIONADO: encontra o menor preço
menor_preco = min(precos)

# >>> ADICIONADO: pega o índice do menor preço
indice_menor = precos.index(menor_preco)
print(indice_menor)

# >>> ADICIONADO: usa o índice para descobrir o nome do produto
produto_mais_barato = produtos[indice_menor]

print(f'O total gasto na compra foi R${total:.2f}')
print(f'{mais_de_mil} produto(s) custam mais de R$1000')
print(f'O produto mais barato foi "{produto_mais_barato}" custando R${menor_preco:.2f}')
