print('\033[1;33m' + '=' * 20, '| Desafio 68 |', '=' * 20 + '\033[m')

'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''

mulheres_menor_vinte = 0
maiores_idade = 0
homens = 0

def linha():
    print('-' * 50)

# Cadastramento de pessoas
while True:

    idade = int(input('Informe sua idade: '))
    linha()

    # Verifica se o usuário está digitando M = Masculino ou F = Feminino
    while True:
        sexo = str(input('Informe seu sexo [M, F]: ')).upper().strip()
        linha()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('Por favor, digite apenas M ou F:')
            linha()

    # Conta homens
    if sexo == 'M':
        homens += 1

    # Conta pessoas maiores de idade
    if idade >= 18:
        maiores_idade += 1

    # Conta mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menor_vinte += 1

    # >>> ALTERADO: validação correta do S ou N (antes estava sempre passando)
    while True:
        continuar = str(input('Você quer continuar "S" para sim e "N" para não? ')).upper().strip()
        linha()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('Por favor digite apenas S para sim ou N para não!')
            linha()

    # >>> ALTERADO: condição simplificada para sair do loop
    if continuar == 'N':
        break

print(f'No total existem {maiores_idade} pessoa(s) maiores de idade')
linha()
print(f'Foram cadastrados {homens} homens no total')
linha()
print(f'No total há {mulheres_menor_vinte} mulheres com menos de 20 anos')
