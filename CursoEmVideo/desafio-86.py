print('\033[1;33m' + '=' * 20 + ' | Desafio 86 | ' + '=' * 20 + '\033[m')

'''
Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado.
No final, mostre na tela com formatação correta.
'''

matriz = []  # Lista principal que armazenará as linhas da matriz
linha = []   # Lista temporária para montar cada linha

# Construção da matriz 3x3
for l in range(3):
    for c in range(3):
        linha.append(int(input(f'Digite um valor para [{l}, {c}]: ')))
    
    # Adiciona uma cópia da linha à matriz
    matriz.append(linha[:])
    linha.clear()  # Limpa a lista temporária para a próxima linha

# Exibição da matriz formatada
print('\n' + '=' * 20, 'MATRIZ', '=' * 20)
for l in range(3):
    for c in range(3):
        print(f'[ {matriz[l][c]:^5} ]', end=' ')
    print()  # Quebra de linha após cada linha da matriz
