print('='*11,'| DESAFIO 07 |', '='*11)
# Desenvolva um program que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média das notas {nota1:.1f} e {nota2:.1f} é {media:.1f}')