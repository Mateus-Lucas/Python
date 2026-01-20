# ==================================================
# AULA — LISTAS COMPOSTAS EM PYTHON
# ==================================================

print('=' * 50)
print(' ' * 12, 'LISTAS COMPOSTAS')
print('=' * 50)

# --------------------------------------------------
# PARTE 1 — LISTA SIMPLES
# --------------------------------------------------
print('\n' + '-' * 50)
print('LISTA SIMPLES')
print('-' * 50)

dados = []
dados.append('Pedro')
dados.append(25)

print(f'Nome: {dados[0]}')
print(f'Idade: {dados[1]}')

# --------------------------------------------------
# PARTE 2 — LISTA COMPOSTA (LISTA DENTRO DE LISTA)
# --------------------------------------------------
print('\n' + '-' * 50)
print('LISTA COMPOSTA')
print('-' * 50)

pessoas = []
pessoas.append(dados[:])  # [:] cria uma CÓPIA da lista

print(f'Pessoas: {pessoas}')

# --------------------------------------------------
# PARTE 3 — ACESSANDO DADOS DA LISTA COMPOSTA
# --------------------------------------------------
print('\n' + '-' * 50)
print('ACESSANDO DADOS')
print('-' * 50)

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0])  # Pedro
print(pessoas[1][1])  # 19
print(pessoas[2][0])  # João
print(pessoas[1])     # ['Maria', 19]

# --------------------------------------------------
# PARTE 4 — CÓPIA CORRETA DE LISTAS
# --------------------------------------------------
print('\n' + '-' * 50)
print('CÓPIA CORRETA DE LISTAS')
print('-' * 50)

teste = []
galera = []

teste.append('Mateus')
teste.append(22)
galera.append(teste[:])  # copia correta

teste[0] = 'Maria'
teste[1] = 28
galera.append(teste[:])  # nova cópia

print(f'Galera: {galera}')

# --------------------------------------------------
# PARTE 5 — PERCORRENDO LISTAS COMPOSTAS
# --------------------------------------------------
print('\n' + '-' * 50)
print('PERCORRENDO LISTAS')
print('-' * 50)

galera = [['João', 19], ['Ana', 25], ['Maria', 45], ['Fernando', 14]]

for p in galera:
    print(f'O nome é {p[0]} e a idade é {p[1]}')

# --------------------------------------------------
# PARTE 6 — EXERCÍCIO COMPLETO (CADASTRO)
# --------------------------------------------------
print('\n' + '=' * 50)
print(' ' * 10, 'CADASTRO DE PESSOAS')
print('=' * 50)

galera = []
dado = []
totmai = totmen = 0

for c in range(3):
    dado.append(input('Informe seu nome: '))
    dado.append(int(input('Informe sua idade: ')))
    
    galera.append(dado[:])  # [:] faz a cópia da lista
    dado.clear()            # limpa a lista auxiliar

print('\n' + '-' * 40)

for p in galera:
    if p[1] >= 21:
        print(f'\033[1;32m{p[0]} é maior de idade\033[m')
        totmai += 1
    else:
        print(f'\033[1;31m{p[0]} é menor de idade\033[m')
        totmen += 1

print('-' * 40)
print(f'Temos {totmai} maiores e {totmen} menores de idade')

# --------------------------------------------------
# FIM DA AULA
# --------------------------------------------------
print('\n' + '=' * 50)
print(' ' * 18, 'FIM')
print('=' * 50)
