print('\033[1;33m' + '=' * 20 + ' | Desafio 94 | ' + '=' * 20 + '\033[m')

''' 
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. 

No final, mostre: 
a) Quantas pessoas cadastradas
b) A média de idade
c) Uma lista com mulheres
d) Uma lista com idade acima da média
'''

pessoas = []
idades = []
mulheres = []

while True:
    nome = str(input('NOME: '))

    # validação do sexo
    sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('ERRO! Digite apenas M ou F: ')).strip().upper()[0]

    idade = int(input('IDADE: '))

    # Criando dicionário
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}

    # Criando cópiia para a lista pessoas
    pessoas.append(pessoa.copy())

    idades.append(idade)

    # Criando lista de nomes de mulheres
    if sexo == 'F':
        mulheres.append(nome)

    # Validação para continuar
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('ERRO! Você deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

# Calculando média
media = sum(idades) / len(pessoas)

print('-=' * 30)
print(f'a) Ao todo temos {len(pessoas)} pessoa(s) cadastradas.')
print(f'b) A média de idade é {media:.1f} anos.')
print(f'c) As mulheres cadastradas foram: {mulheres}')

print('d) Lista das pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        print(f'   {p["nome"]} ({p["idade"]} anos)')
