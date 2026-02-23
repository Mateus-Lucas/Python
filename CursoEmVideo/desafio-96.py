print('\033[1;33m' + '=' * 20 + ' | Desafio 96 | ' + '=' * 20 + '\033[m')

''' Faça um programa que tenha função chamada area(), que
receba as dimensões de um terreno retangular (largula e 
comprimento) e mostre a área de terreno.'''


# CÓDIGO GUANABARA
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')


# PROGRAMA PRINCIPAL
print(' Controle de terrenos')
print('' * 20)
l = float(input('Largura (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)



# # CÓDIGO PESSOAL
# print(' CONTROLE DE TERRENOS')
# print('-=' * 15)

# # Função que calcula a área
# def area(a, b):
#     print(f'A área de um terreno {a}x{b} é de {a*b}m²')

# # Chamando função com os valores para o usuário digitar
# area(
#     a = float(input('LARGURA (m):  ')), 
#     b = float(input('COMPRIMENTO (m): '))
# )