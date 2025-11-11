print('=' * 20, '| Desafio 61 |', '=' * 20)

"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de 
uma PA, mostrando os 10 primeiros termos da progressão usando
a estrutura while.
"""

from time import sleep

def linha():
    print('\033[1;33m=\033[m' * 40)

linha()
print(' ' * 10, '\033[1;33m10 TERMOS DE UMA PA\033[m')
linha()

# p1 = primeiro termo | r = razão | c = contador | t = termo

p1 = int(input('\033[1;36mInforme o primeiro termo:\033[m '))
r = int(input('\033[1;36mInforme a razão dessa PA:\033[m '))
c = 1

print('\n\033[1;34mCalculando a progressão...\033[m\n')
sleep(1)

linha()
while c <= 10:
    t = p1 + (c - 1) * r
    print(f'\033[1;33m{c}º termo\033[m = \033[1;32m{t}\033[m')
    sleep(0.2)
    c += 1
linha()

print('\n\033[1;32mFIM DA PROGRESSÃO ARITMÉTICA!\033[m')
