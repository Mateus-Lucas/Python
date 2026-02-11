# ============================================================
# 🎓 AULA COMPLETA — DICIONÁRIOS EM PYTHON
# ============================================================

# 🎨 CÓDIGOS DE COR (ANSI)
azul = '\033[1;34m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
vermelho = '\033[1;31m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
reset = '\033[0m'

print(roxo + '=' * 60)
print('📘 AULA DE DICIONÁRIOS EM PYTHON'.center(60))
print('=' * 60 + reset)


# ============================================================
# 🔹 1) O QUE É UM DICIONÁRIO?
# ============================================================

print(ciano + '\n📌 1) CRIANDO UM DICIONÁRIO' + reset)

# Dicionário usa { } e trabalha com CHAVE : VALOR
pessoa = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(verde + 'Dicionário criado:' + reset, pessoa)

print(amarelo + '\n💡 Estrutura:' + reset)
print('   { chave : valor }')


# ============================================================
# 🔹 2) ACESSANDO VALORES
# ============================================================

print(ciano + '\n📌 2) ACESSANDO VALORES' + reset)

print(verde + f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.' + reset)

print(amarelo + '\n💡 Para acessar usamos: dicionario["chave"]' + reset)


# ============================================================
# 🔹 3) MÉTODOS IMPORTANTES
# ============================================================

print(ciano + '\n📌 3) MÉTODOS IMPORTANTES' + reset)

print(azul + '\n🔑 .keys() → retorna apenas as CHAVES' + reset)
print(pessoa.keys())

print(azul + '\n📦 .values() → retorna apenas os VALORES' + reset)
print(pessoa.values())

print(azul + '\n📚 .items() → retorna CHAVE + VALOR' + reset)
print(pessoa.items())


# ============================================================
# 🔹 4) ALTERANDO DADOS
# ============================================================

print(ciano + '\n📌 4) ALTERANDO DADOS' + reset)

# ✏️ Alterando valor
pessoa['nome'] = 'Leandro'
print(verde + '✔ Nome alterado!' + reset)

# ➕ Adicionando nova chave
pessoa['peso'] = 98.5
print(verde + '✔ Peso adicionado!' + reset)

# ❌ Removendo chave
del pessoa['sexo']
print(vermelho + '✖ Sexo removido!' + reset)

print(amarelo + '\n📌 Dicionário atualizado:' + reset, pessoa)


# ============================================================
# 🔹 5) PERCORRENDO DICIONÁRIOS
# ============================================================

print(ciano + '\n📌 5) PERCORRENDO DICIONÁRIOS' + reset)

print(azul + '\n🔁 Apenas CHAVES:' + reset)
for k in pessoa.keys():
    print('   🔹', k)

print(azul + '\n🔁 Apenas VALORES:' + reset)
for v in pessoa.values():
    print('   🔸', v)

print(azul + '\n🔁 CHAVE e VALOR juntos (mais usado):' + reset)
for k, v in pessoa.items():
    print(f'   📌 {k} = {v}')


# ============================================================
# 📘 LISTA COM DICIONÁRIOS
# ============================================================

print(roxo + '\n' + '=' * 60)
print('📦 LISTA COM DICIONÁRIOS'.center(60))
print('=' * 60 + reset)

brasil = []

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(verde + '\nLista completa:' + reset, brasil)

print(amarelo + '\n📌 Acessando dados específicos:' + reset)
print('   🗺 UF do primeiro estado:', brasil[0]['uf'])
print('   🏷 Sigla do segundo estado:', brasil[1]['sigla'])


# ============================================================
# ⚠️ 6) IMPORTÂNCIA DO .copy()
# ============================================================

print(roxo + '\n' + '=' * 60)
print('⚠️  CUIDADO COM REFERÊNCIA DE MEMÓRIA'.center(60))
print('=' * 60 + reset)

estado = {}
brasil = []

for c in range(2):
    print(ciano + f'\n🌎 Cadastro {c+1}' + reset)
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ')
    
    # 🔥 Aqui está o segredo:
    brasil.append(estado.copy())

print(verde + '\n📋 Estados cadastrados:' + reset)

for e in brasil:
    print('   ', end='')
    for v in e.values():
        print(v, end=' ')
    print()

print(amarelo + '\n💡 .copy() evita que todos os elementos apontem')
print('   para o mesmo espaço de memória!' + reset)


print(roxo + '\n' + '=' * 60)
print('🏁 FIM DA AULA — VOCÊ DOMINOU DICIONÁRIOS 🧠🔥'.center(60))
print('=' * 60 + reset)
