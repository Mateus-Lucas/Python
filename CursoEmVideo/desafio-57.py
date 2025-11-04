print('=' * 20, '| Desafio 57 |', '=' * 20)

"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = input('Informe o seu sexo [M/F]: ').strip().upper()

while sexo not in ['M', 'F']:
    sexo = input('\033[1;31mSexo não reconhecido.\033[m Digite apenas M ou F: ').strip().upper()

print(f'\033[1;32mSexo registrado com sucesso: {sexo}\033[m')
