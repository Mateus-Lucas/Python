print('\033[1;33m' + '=' * 20 + ' | Desafio 90 | ' + '=' * 20 + '\033[m')

''' Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrtura na tela'''

# Montando o dicionário já com a entrada do usuário
aluno = {'nome': str(input('NOME: ')), 'media': float(input('MÉDIA: '))}
situacao = ''

# Verificando a situação do aluno
if aluno['media'] < 5:
    situacao = 'REPROVADO'
elif aluno['media'] < 7:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'APROVADO'

# Adicionando a situação do aluno ao dicionário
aluno['situacao'] = situacao

print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')