print('=' * 20, '| DESAFIO 37 |', '=' * 20)

"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:

1 - Binário
2 - Octal
3 - Hexadecimal
"""

print('-=' * 27)
print(' ' * 14, '\033[1;35mCONVERSOR DE BASES\033[m')
print('-=' * 27)

numero = int(input('Informe um número inteiro: '))

print('''Escolha a base de conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')

base = int(input('Sua opção: '))

if base == 1:
    resultado = bin(numero)[2:]  # [2:] remove o prefixo '0b'
    nome = 'Binário'
elif base == 2:
    resultado = oct(numero)[2:]  # [2:] remove o prefixo '0o'
    nome = 'Octal'
elif base == 3:
    resultado = hex(numero)[2:]  # [2:] remove o prefixo '0x'
    nome = 'Hexadecimal'
else:
    print('\033[1;31mOpção inválida! Tente novamente.\033[m')
    exit()

print(f'O número {numero} convertido para {nome} é \033[1;32m{resultado.upper()}\033[m')
