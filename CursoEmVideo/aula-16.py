# ======================================================
# 🧠 AULA: TUPLAS EM PYTHON
# ======================================================

# 🎯 Tuplas são estruturas de dados IMUTÁVEIS
# Depois de criadas, NÃO podem ser alteradas

print('\033[1;36m' + '=' * 55)
print('        📚 AULA SOBRE TUPLAS EM PYTHON')
print('=' * 55 + '\033[m\n')

# ======================================================
# 📦 CRIANDO UMA TUPLA
# ======================================================

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print('\033[1;33mTupla criada:\033[m', lanche, '\n')

# ======================================================
# 🔍 ACESSO AOS ELEMENTOS
# ======================================================

print('\033[1;34m🔍 ACESSANDO ELEMENTOS DA TUPLA\033[m')

print(f'\033[32mÍndice 2:\033[m {lanche[2]}')
print(f'\033[32mDo índice 0 ao 1:\033[m {lanche[0:2]}')
print(f'\033[32mDo índice 1 até o final:\033[m {lanche[1:]}')
print(f'\033[32mDo início até o índice 1:\033[m {lanche[:2]}')
print(f'\033[32mDois últimos elementos:\033[m {lanche[-2:]}')
print(f'\033[32mÚltimo elemento:\033[m {lanche[-1]}\n')

# ======================================================
# 📏 TAMANHO DA TUPLA
# ======================================================

print('\033[1;34m📏 TAMANHO DA TUPLA\033[m')
print(f'A tupla possui \033[33m{len(lanche)}\033[m elementos\n')

# ======================================================
# 🔒 IMUTABILIDADE
# ======================================================

print('\033[1;34m🔒 IMUTABILIDADE\033[m')
print('❌ Não é possível alterar valores dentro da tupla')

# lanche[1] = 'Refrigerante'  # Isso causaria ERRO
print('\n')

# ======================================================
# 🔁 PERCORRENDO A TUPLA (FORMA SIMPLES)
# ======================================================

print('\033[1;34m🔁 PERCORRENDO A TUPLA (SEM ÍNDICE)\033[m')

for comida in lanche:
    print(f'🍽️ Eu vou comer \033[32m{comida}\033[m')

print('\n\033[1;33m😋 Comi pra caramba!\033[m\n')

# ======================================================
# 🔢 PERCORRENDO A TUPLA COM ÍNDICE
# ======================================================

print('\033[1;34m🔢 PERCORRENDO A TUPLA COM ÍNDICE\033[m')

for cont in range(0, len(lanche)):
    print(f'📌 Índice {cont} → \033[32m{lanche[cont]}\033[m')

print('\n')

# ======================================================
# 🔃 ORDENANDO UMA TUPLA (SEM ALTERAR A ORIGINAL)
# ======================================================

print('\033[1;34m🔃 TUPLA ORDENADA (sorted)\033[m')
print(sorted(lanche), '\n')

# ======================================================
# ➕ OPERAÇÕES COM TUPLAS
# ======================================================

print('\033[1;34m➕ OPERAÇÕES COM TUPLAS\033[m')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(f'Tupla A: {a}')
print(f'Tupla B: {b}')
print(f'A + B = \033[32m{c}\033[m')

print(f'\n🔎 O número 5 aparece \033[33m{c.count(5)}\033[m vezes')
print(f'📍 O número 8 está na posição \033[33m{c.index(8)}\033[m\n')

# ======================================================
# 🧍‍♂️ TUPLA COM TIPOS DIFERENTES
# ======================================================

print('\033[1;34m🧍‍♂️ TUPLAS COM TIPOS DIFERENTES\033[m')

pessoa = ('Gustavo', 39, 'M', 99.88)
print('Tupla pessoa:', pessoa)

# ======================================================
# 🗑️ APAGANDO UMA TUPLA
# ======================================================

print('\033[1;34m🗑️ EXCLUINDO UMA TUPLA\033[m')
print('✅ É possível apagar a tupla inteira')
print('❌ NÃO é possível apagar um item específico')

del pessoa
# del pessoa[0]  # Isso causaria ERRO

print('\n\033[1;36m' + '=' * 55)
print('        ✅ FIM DA AULA DE TUPLAS')
print('=' * 55 + '\033[m')
