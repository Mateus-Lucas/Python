# 05 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média 
# alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_aluno = float(input('Informe a nota do aluno: '))

if nota_aluno == 10:
    print(f'O aluno foi aprovado com distinção nota {nota_aluno}')

elif nota_aluno >= 7: 
    print(f'O aluno foi aprovado com a nota {nota_aluno}')

else:
    print(f'O aluno foi reprovado com a nota {nota_aluno}')
