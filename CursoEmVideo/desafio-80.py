# Título formatado em amarelo (código ANSI)
print('\033[1;33m' + '=' * 20, '| Desafio 80 |', '=' * 20 + '\033[m')

'''
Crie um programa onde o usuário digita cinco valores numéricos
e eles são inseridos em uma lista já na posição correta,
sem utilizar o método sort().
No final, mostre a lista ordenada.
'''

# Lista que irá armazenar os números já ordenados
numeros = []

# Loop para ler exatamente 5 números
for c in range(5):
    num = int(input('Digite um número: '))

    # Se for o primeiro número OU se for maior que o último da lista
    # ele pode ser adicionado diretamente no final
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Número inserido no final da lista')

    # Caso contrário, precisamos encontrar a posição correta
    else:
        pos = 0

        # Percorre a lista até encontrar onde inserir
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Foi inserido o número {num} na posição {pos}')
                break
            pos += 1

# Exibe a lista final ordenada
print(numeros)
