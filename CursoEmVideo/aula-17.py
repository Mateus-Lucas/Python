# ==========================================
# AULA: LISTAS EM PYTHON 🧠🐍
# ==========================================

def titulo(texto):
    print('\033[1;36m' + '\n' + '=' * 50)
    print(f'{texto:^50}')
    print('=' * 50 + '\033[m\n')

# ==========================================
# 1️⃣ CRIANDO UMA LISTA
# ==========================================

titulo('1️⃣ CRIANDO UMA LISTA')

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(f'Lista inicial: {lanche}')

# ==========================================
# 2️⃣ ALTERANDO ELEMENTOS
# ==========================================

titulo('2️⃣ ALTERANDO ELEMENTOS DA LISTA')

lanche[3] = 'Biscoito'
print(f'Alterando índice 3: {lanche}')

# ==========================================
# 3️⃣ ADICIONANDO ELEMENTOS
# ==========================================

titulo('3️⃣ ADICIONANDO ELEMENTOS')

lanche.append('Pastel')
print(f'Após append: {lanche}')

lanche.insert(0, 'Cachorro-quente')
print(f'Após insert: {lanche}')

# ==========================================
# 4️⃣ REMOVENDO ELEMENTOS
# ==========================================

titulo('4️⃣ REMOVENDO ELEMENTOS')

del lanche[3]
print(f'Após del: {lanche}')

lanche.pop()
print(f'Após pop: {lanche}')

if 'Pizza' in lanche:
    lanche.remove('Pizza')

print(f'Após remove: {lanche}')

# ==========================================
# 5️⃣ LISTA COM RANGE
# ==========================================

titulo('5️⃣ LISTA COM RANGE')

valores = list(range(4, 11))
print(f'Lista criada com range: {valores}')

# ==========================================
# 6️⃣ ORDENAÇÃO
# ==========================================

titulo('6️⃣ ORDENAÇÃO DE LISTAS')

valores = [8, 2, 5, 4, 9, 3, 0]
print(f'Lista original: {valores}')

valores.sort()
print(f'Ordem crescente: {valores}')

valores.sort(reverse=True)
print(f'Ordem decrescente: {valores}')

# ==========================================
# 7️⃣ TAMANHO DA LISTA
# ==========================================

titulo('7️⃣ TAMANHO DA LISTA')

print(f'A lista possui {len(valores)} elementos')

# ==========================================
# 8️⃣ MANIPULAÇÃO COMPLETA
# ==========================================

titulo('8️⃣ EXEMPLO COMPLETO')

num = [2, 5, 9, 1]
print(f'Lista inicial: {num}')

num[2] = 2
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)

if 4 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

print(f'Lista final: {num}')
print(f'Total de elementos: {len(num)}')

# ==========================================
# 9️⃣ ENTRADA DE DADOS + ENUMERATE
# ==========================================

titulo('9️⃣ ENTRADA DE DADOS NA LISTA')

valores = []

for cont in range(5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

print()

for c, v in enumerate(valores):
    print(f'Posição {c} → Valor {v}')

print('Fim da leitura.')

# ==========================================
# 🔟 CÓPIA DE LISTAS
# ==========================================

titulo('🔟 CÓPIA DE LISTAS (IMPORTANTE)')

a = [2, 3, 4, 7]

# b = a     # ❌ ligação
b = a[:]    # ✅ cópia

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
