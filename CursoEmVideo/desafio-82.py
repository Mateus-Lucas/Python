print('\033[1;33m' + '=' * 20, '| Desafio 82 |', '=' * 20 + '\033[m')

''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas valores pares
e os valores imparesx digitados respectivamente. Ao final, mostre o conteúdo das três listas geradas'''

numeros = []
impares = []
pares = []

while True:
    numero = int(input('Digite um valor :'))
    numeros.append(numero)
    continuar = str(input('Deseja continuar? ')).strip().upper()[0]

    # Criando listar para pares e ímpares
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    
    while continuar not in 'SN':
        continuar = str(input('Por favor digite apenas [S/N]! Quer continuar? ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Todos os números: {numeros}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
    


