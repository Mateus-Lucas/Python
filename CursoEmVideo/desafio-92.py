print('\033[1;33m' + '=' * 20 + ' | Desafio 92 | ' + '=' * 20 + '\033[m')

'''
Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-os (com idade) em um dicionário. Se a CTPS
for diferente de zero, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime

ano_atual = datetime.now().year

# Abrindo dicionário e pedindo informações para o usuário
pessoa = {
    'nome': input('Nome: '),
    'idade': ano_atual - int(input('Ano de nascimento: ')),
    'carteira_trabalho': int(input('Carteira de trabalho (0 não tem): '))
}

# If que identifica usuário que possui ctps e faz o calculo da sua aposentadoria
if pessoa['carteira_trabalho'] > 0:
    pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['ano_contratacao'] + 35 - ano_atual)

print('-=' * 30)

for k, v in pessoa.items():
    print(f'{k.capitalize()}: {v}')
