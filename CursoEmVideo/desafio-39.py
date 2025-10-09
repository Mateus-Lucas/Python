print('=' * 20, '| Desafio 39 |' ,'=' * 20)

'''
 Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

print('-=' * 20)
print(' ' * 7, '\033[1;33mRELATÓRIO DE ALISTAMENTO\033[m')
print('-=' * 20)

ano_nascimento = int(input('Informe o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
ano = 'anos'

if idade < 18:
    if 18 - idade == 1:
        ano = 'ano'
    print(f'\033[1;33mSua idade é de {idade} anos e você deve se alistar em {18 - idade} {ano}.\033[m')
elif idade > 18:
    if idade - 18 == 1:
        ano = 'ano'
    print(f'\033[1;32mSua idade é de {idade} anos e você deveria ter se alistado há {idade - 18} {ano} atrás.\033[m')
else:
    print(f'\033[1;31mCORRA! Pois você deve se alistar imediatamente, completando 18 anos este ano!\033[m')
