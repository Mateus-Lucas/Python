print('='*11,'| DESAFIO 19 |', '='*11)
'''Um professor quer sortear um dos seus quatros alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''

from random import choice

aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)

print(f'O aluno escolhido foi {escolhido}')