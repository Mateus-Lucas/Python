print('\033[1;33m' + '=' * 20, '| Desafio 78 |', '=' * 20 + '\033[m')

''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual o maior e o menor valor digitado e as suas respectivas posições na lista.'''

numeros = []

# Criando uma lista com 5 números
for i in range(5):
    num = int(input(f'Digite um número para a posição {i}: '))
    numeros.append(num)

# Criando maior e menor valores
maior = max(numeros)
menor = min(numeros)

print(f'\nOs números digitados foram: {numeros}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')

# Percorre a lista usando enumerate para obter:
# i -> índice (posição)
# v -> valor armazenado naquela posição
for i, v in enumerate(numeros):
     # Verifica se o valor da posição atual é igual ao maior valor da lista
    if v == maior:
        print(f'{i} ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i} ', end='')