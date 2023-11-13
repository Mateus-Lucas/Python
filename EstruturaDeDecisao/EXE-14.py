# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se
# o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

p1 = float(input('informe a nota da P1: '))
p2 = float(input('informe a nota da P2: '))

media = (p1 + p2)/2
conceito = ''
situacao = ''

if media >= 6:
    situacao = 'APROVADO'
    if media >= 9:
       conceito = 'A'
    elif media >= 7.5:
       conceito = 'B'
    else: 
       conceito = 'C'
else: 
    situacao = 'REPROVADO'
    if media >= 4:
        conceito = 'D'
    else: 
        conceito = 'E'
  
print(f'Notas: P1= {p1} P2= {p2}')
print(f'Média: {media}')
print(f'{situacao} com o conceito {conceito}')
