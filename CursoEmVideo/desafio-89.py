print('\033[1;33m' + '=' * 20 + ' | Desafio 89 | ' + '=' * 20 + '\033[m')

'''
Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

alunos = []  # Lista principal
aluno = []   # Lista auxiliar

# ===============================
# CADASTRO DOS ALUNOS
# ===============================
while True:
    aluno.append(input('Informe o nome do aluno: '))
    aluno.append(float(input('Informe a primeira nota: ')))
    aluno.append(float(input('Informe a segunda nota: ')))
    
    alunos.append(aluno[:])  # Copiando aluno para lista principal
    aluno.clear()            # Limpando lista auxiliar

    continuar = input('Você quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Digite apenas S ou N: ').strip().upper()[0]
    if continuar == 'N':
        break

# ===============================
# EXIBIÇÃO DO BOLETIM
# ===============================
print('\n' + '-' * 40)
print(f'{"No.":<4}{"Nome":<15}{"Média":>8}')
print('-' * 40)

for i, a in enumerate(alunos):
    media = (a[1] + a[2]) / 2
    print(f'{i:<4}{a[0]:<15}{media:>8.1f}')

# ===============================
# CONSULTA INDIVIDUAL DE NOTAS
# ===============================
while True:
    opcao = int(input('\nMostrar notas de qual aluno? (999 interrompe): '))
    
    if opcao == 999:
        print('FINALIZANDO...')
        break
    
    if opcao < 0 or opcao >= len(alunos):
        print('Aluno inválido!')
    else:
        print(f'Notas de {alunos[opcao][0]}: {alunos[opcao][1]} e {alunos[opcao][2]}')
