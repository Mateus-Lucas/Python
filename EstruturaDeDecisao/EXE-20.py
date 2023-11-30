# 20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada
# por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
nota3 = float(input('Informe a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f'Aprovado com Distinção com a média {media:.2f}')
elif media >= 7:
    print(f'Aprovado com a média {media:.2f}')
else:
    print(f'Reprovado com a média {media:.2f}')