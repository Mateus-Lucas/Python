print('\033[1;33m' + '=' * 20, '| Desafio 68 |' , '=' * 20 + '\033[m')

''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
jogador PERDER, mostrando o total de vitórias que ele conquistou no final do jogo'''

from random import randint

def linha():
    print('-' * 40)

vitorias = 0

while True:
    # escolha par ou ímpar
    while True:
        try:
            escolha = int(input(
                'Escolha par ou ímpar:\n'
                '[1] para par\n'
                '[2] para ímpar\n'
            ))
            if escolha in (1, 2):
                break
            else:
                print('Opção inválida. Digite 1 ou 2.')
        except ValueError:
            print('Entrada inválida. Digite um número (1 ou 2).')

    computador = 'ímpar' if escolha == 1 else 'par'
    linha()
    print(f'COMPUTADOR: Certo, eu escolho {computador}')

    # número do jogador (com validação)
    while True:
        try:
            quant_jogador = int(input('Informe um valor de 1 a 10 para jogar: '))
            if 1 <= quant_jogador <= 10:
                break
            else:
                print('Valor fora do intervalo. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')

    # número do computador e soma
    quant_computador = randint(1, 10)
    soma = quant_computador + quant_jogador

    linha()
    print(f'O computador escolheu {quant_computador} e você escolheu {quant_jogador} resultando em {soma}')

    # determina par/ímpar do resultado
    resultado = 'par' if soma % 2 == 0 else 'ímpar'

    # verifica se o jogador venceu
    if (escolha == 1 and resultado == 'par') or (escolha == 2 and resultado == 'ímpar'):
        vitorias += 1
        print('Você venceu! Vamos jogar novamente...')
        linha()
        # continua o loop para próxima rodada
    else:
        print('Você perdeu, que pena )=')
        print(f'Você ganhou no total {vitorias} vezes')
        break
