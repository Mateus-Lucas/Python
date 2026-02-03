print('\033[1;33m' + '=' * 20 + ' | Desafio 87 | ' + '=' * 20 + '\033[m')

''' Aprimore o desafio anterior, mostrando no final: 
a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha '''

matriz = []
soma_pares = 0
soma_terceira_coluna = 0

# Leitura da matriz
for l in range(3):
    linha = []
    for c in range(3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        linha.append(valor)

        # Soma dos pares
        if valor % 2 == 0:
            soma_pares += valor

        # Soma da terceira coluna (índice 2)
        if c == 2:
            soma_terceira_coluna += valor

    matriz.append(linha)

# Exibindo a matriz
print('\nMatriz digitada:')
for l in range(3):
    for c in range(3):
        print(f'[ {matriz[l][c]:^5} ]', end=' ')
    print()

# Maior valor da segunda linha (índice 1)
maior_segunda_linha = max(matriz[1])

# Resultados finais
print(f'\nA soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')
