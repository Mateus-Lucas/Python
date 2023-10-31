#  03 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#  Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite M para sexo masculino e F para feminino: ')

if sexo == 'M':
    print('M - Sexo: Masculino')
elif sexo == 'F':
    print('F - Sexo: Feminino')
else: 
    print('Sexo inválido')

