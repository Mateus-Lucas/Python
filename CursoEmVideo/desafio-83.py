print('\033[1;33m' + '=' * 20 + ' | Desafio 83 | ' + '=' * 20 + '\033[m')

'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
O programa deve verificar se os parênteses estão abertos e fechados corretamente.
'''

expressao = input('Digite uma expressão: ')

pilha = []

# Variável de controle de validade
valida = True

# Percorre cada caractere da expressão
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')    # Abre parêntese
    elif simbolo == ')':
        if pilha:
            pilha.pop()      # Fecha parêntese corretamente
        else:
            valida = False   # Tentou fechar sem abrir
            break

# Expressão válida se não houve erro e a pilha estiver vazia
if valida and not pilha:
    print('Expressão VÁLIDA ✔️')
else:
    print('Expressão INVÁLIDA ❌')
