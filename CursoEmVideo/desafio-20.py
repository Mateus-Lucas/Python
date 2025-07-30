print('='*11,'| DESAFIO 20 |', '='*11)
'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatros alunos e mostre a ordemsorteada.'''

from random import shuffle

aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

print(f'A ordem sorteada dos alunos é {alunos}')

