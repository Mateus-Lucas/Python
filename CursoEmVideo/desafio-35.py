print('=' * 20, '| Desafio 20 |', '=' * 20)

"""
 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
 podem ou não formar um triângulo
"""

print('\033[1;34m' + '-=-' * 20 + '\033[m')
print('\033[1;36m{:^60}\033[m'.format('ANALISADOR DE TRIÂNGULOS'))
print('\033[1;34m' + '-=-' * 20 + '\033[m')

# Entrada de dados com destaque
a = float(input('\033[4;30;46mPrimeiro segmento: \033[m '))
b = float(input('\033[4;30;46mSegundo segmento: \033[m '))
c = float(input('\033[4;30;46mTerceiro segmento: \033[m '))

# Verificação da condição do triângulo
print('\n\033[1;35mResultado:\033[m')
if a + b > c and a + c > b and b + c > a:
    print('\033[1;32mOs segmentos acima PODEM formar um triângulo!\033[m')
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM formar um triângulo!\033[m')
