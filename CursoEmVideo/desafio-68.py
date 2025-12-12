print('\033[1;33m' + '=' * 20, '| Desafio 68 |' , '=' * 20 + '\033[m')

''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
jogador PERDER, mostrando o total de vitórias que ele conquistou no final do jogo'''

from random import randint

v = 0  # contador de vitórias

while True:  # loop principal do jogo
    # --- validação do número digitado pelo jogador ---
    while True:
        entrada = input('Diga um valor (0 a 10): ').strip()
        if entrada.isdigit() and 0 <= int(entrada) <= 10:
            jogador = int(entrada)
            break
        print('Valor inválido. Digite um número entre 0 e 10.')

    computador = randint(0, 10)  # número aleatório do computador
    total = jogador + computador  # soma dos valores

    # --- validação da escolha par/ímpar ---
    while True:
        tipo = input('Par ou Ímpar [P/I]: ').strip().upper()
        if tipo != '' and tipo[0] in 'PI':
            tipo = tipo[0]
            break
        print('Opção inválida. Digite P ou I.')

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')

    # --- determina se o total é par ou ímpar ---
    resultado = 'P' if total % 2 == 0 else 'I'

    # --- verifica vitória ou derrota ---
    if tipo == resultado:
        v += 1
        print('Você VENCEU! Vamos jogar novamente...')
        print('-' * 40)
    else:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {v} vezes.')
        break
