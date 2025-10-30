print('=' * 20, '| Desafio 54 |', '=' * 20)

"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f'Informe o ano de nascimento da {i}ª pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'\033[1;32mNo total {maiores} pessoa(s) já são maiores de idade.\033[m')
print(f'\033[1;31mE {menores} pessoa(s) ainda são menores de idade.\033[m')
