print('=' * 20, '| Desafio 41 |' ,'=' * 20)

'''
 A Confederação Nacional de Natação precisa de um programa que 
 leia o ano de nascimento de um atleta e mostre sua categoria. 
 de acordo com a idade:
 - Até 9 anos: MIRIM        - Até 19 anos: JUNIOR
 - Até 14 anos: INFANTIL    - Até 25 anos: SÊNIOR
                            - Acima: MASTER
'''

from datetime import date

print('-=' * 21)
print(' ' * 10,'CATEGORIA DE ATLETAS')
print('-=' * 21)

# Pede o ano de nascimento do atleta
ano_nascimento = int(input('Informe seu ano de nascimento: '))

# Calcula a idade
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

categoria = ''

# Determina a categoria com base na idade
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

# Imprime o resultado
print(f'Com a idade de {idade} anos você pode competir na categoria {categoria}')