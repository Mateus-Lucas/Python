print('=' * 20, '| Desafio 56 |', '=' * 20)

'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos
'''

from time import sleep

print('\033[1;36m' + '=' * 20, '| Desafio 56 |', '=' * 20 + '\033[m')
print('\033[1;37mVamos coletar informações de 4 pessoas.\033[m')
print('-' * 60)

soma_idades = 0
cont = 0
homem_mais_velho = ''
idade_mais_velho = 0
mulheres_menos_20 = 0

for i in range(1, 5):
    print(f'\n\033[1;34m>>> {i}ª PESSOA <<<\033[m')
    print('-' * 30)

    nome = input('\033[1;37mNome: \033[m').strip().title()
    idade = int(input('\033[1;37mIdade: \033[m'))

    sexo = input('\033[1;37mSexo [M/F]: \033[m').strip().upper()
    while sexo not in ('M', 'F'):
        print('\033[1;31mEntrada inválida!\033[m Digite apenas M ou F.')
        sexo = input('\033[1;37mSexo [M/F]: \033[m').strip().upper()

    soma_idades += idade
    cont += 1

    if sexo == 'M':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    print('\033[1;32mDados registrados com sucesso!\033[m')
    sleep(0.5)

print('\n\033[1;36m' + '=' * 20, 'RESULTADOS', '=' * 20 + '\033[m')
media = soma_idades / cont
sleep(0.5)

print(f'\033[1;33mA média de idade do grupo é {media:.1f} anos.\033[m')
print(f'\033[1;33mO homem mais velho é {homem_mais_velho if homem_mais_velho else "nenhum"}.\033[m')
print(f'\033[1;33mHá {mulheres_menos_20} mulher(es) com menos de 20 anos.\033[m')
print('\033[1;36m' + '=' * 56 + '\033[m')
