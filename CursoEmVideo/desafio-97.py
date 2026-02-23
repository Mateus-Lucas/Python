print('\033[1;33m' + '=' * 20 + ' | Desafio 96 | ' + '=' * 20 + '\033[m')

''' Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

# CÓDIGO GUANABARA
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# # CÓDIGO PESSOAL 
# def escreva(a):
#     print('~' * len(a))
#     print(a)
#     print('~' * len(a))


# # PROGRAMA PRINCIPAL
escreva('Mateus')
escreva('Lucas')
escreva('Ferreira')
escreva('Rodrigues')