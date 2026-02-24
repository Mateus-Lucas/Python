print('\033[1;33m' + '=' * 20 + ' | Desafio 98 | ' + '=' * 20 + '\033[m')

'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contador personalizada
'''
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1    
    print('-=' * 20)
    print(f'contador de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# # CÓDIGO PESSOAL
# from time import sleep

# def contador(inicio, fim, passo):
#     print('-=' * 15)
#     # evita passo zero
#     if passo == 0:
#         passo = 1
#     # define direção automática
#     if inicio < fim:
#         passo = abs(passo)
#     else:
#         passo = -abs(passo)
#     # ajuste para incluir o fim
#     for i in range(inicio, fim + (1 if passo > 0 else -1), passo):
#         print(f'\033[1;33m{i}\033[m', end=' ')
#         sleep(0.3)
#     print()
#     print('-=' * 15)


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agira é sua vez de personalizar')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))

contador(i, f, p)