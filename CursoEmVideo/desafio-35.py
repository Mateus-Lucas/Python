print('=' * 20, '| Desafio 20 |' ,'=' * 20)

'''
 Desenvolvea um programa que leia o comprimento de três retas e diga ao usuário se elas
 podem ou não formar um triângulo
'''
print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

# Verifica a condição para formar um triângulo
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos formam um triângulo')
else:
    print('Os segmentos não formam um triângulo')
