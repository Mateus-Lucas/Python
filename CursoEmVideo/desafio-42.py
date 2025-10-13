print('=' * 20, '| Desafio 42 |', '=' * 20)

"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de 
mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

def linha():
    print('\033[1;34m' + '-=-' * 20 + '\033[m')

linha()
print('\033[1;36m{:^60}\033[m'.format('ANALISADOR DE TRIÂNGULOS'))
linha()

# Entrada de dados com destaque
a = float(input('\033[4;30;46mPrimeiro segmento: \033[m '))
b = float(input('\033[4;30;46mSegundo segmento: \033[m '))
c = float(input('\033[4;30;46mTerceiro segmento: \033[m '))

# Verificação da condição do triângulo
print('\n\033[1;35mResultado:\033[m')

if a + b > c and a + c > b and b + c > a:
    print('\033[1;32mOs segmentos acima PODEM formar um triângulo!\033[m')
    if a == b == c:
        print('➡️  Esse triângulo é \033[1;33mEQUILÁTERO\033[m')
    elif a == b or b == c or a == c:
        print('➡️  Esse triângulo é \033[1;33mISÓSCELES\033[m')
    else:
        print('➡️  Esse triângulo é \033[1;33mESCALENO\033[m')
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM formar um triângulo!\033[m')
