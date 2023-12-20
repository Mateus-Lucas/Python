# 03 - Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

while True:
    nome = input('Informe o nome: ')
    idade = int(input('Informe a sua idade: '))
    salario = float(input('Informe o seu salário: '))
    sexo = input('Informe o sexo M ou F: ').upper()
    estado_civil = input('Informe o estado civil: \n s - Solteiro \n c - Casado \n v - Viúvo \n d - Divorciado \n')

    tamanho_nome = len(nome)

    if tamanho_nome > 3 and 0 <= idade <= 150 and salario >= 0 and sexo in ['M', 'F'] and estado_civil in ['s', 'c', 'v', 'd']:
        print('-----------| Informações da pessoa |-----------')
        print(f'Nome: {nome}\nIdade: {idade}\nSalário: R${salario:.2f}\nSexo: {"Masculino" if sexo == "M" else "Feminino"}\nEstado Civil: {estado_civil}')
        break
    else:
        print('Alguma informação é inválida. Por favor, insira os dados novamente.\n')




