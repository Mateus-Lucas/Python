print('=' * 20, '| Desafio 40 |' ,'=' * 20)

'''
 Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:
 - Média abaixo de 5.0: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO
'''

print('-=' * 21)
print(' ' * 7,'RESULTADO FINAL DO SEMESTRE')
print('-=' * 21)

n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))
media = (n1 + n2) / 2

print('-' * 21)
print(f'Sua média foi de {media}')
print('-' * 21)

if media < 5:
    print('\033[1;31mInfelizmente você foi REPROVADO\033[m')
elif media < 7:
    print('\033[1;33mVocê está de RECUPERAÇÃO, estude mais!\033[m')
else:
    print('\033[1;32mMeus parabéns, você foi APROVADO\033[m') 