print('=' * 20, '| Desafio 45 |' ,'=' * 20)

''' Crie um programa que faça o computador jogar jokenpô com você'''

from random import randint

# Lista das opções
opcoes = ['Pedra', 'Papel', 'Tesoura']
# Emojis para cada opção
emojis = ['🪨', '📄', '✂️']

# Função para linha decorativa
def linha():
    print('\033[1;34m' + '--' * 15 + '\033[m')  # Azul negrito

# Cabeçalho
linha()
print(f'\033[1;33m{"JOKENPÔ":^31}\033[m')  # Amarelo
linha()

# Entrada do jogador
num_jogador = int(input('Escolha uma opção: \n[1] Pedra 🪨 \n[2] Papel 📄 \n[3] Tesoura ✂️\n'))

# Verificação de entrada
if num_jogador not in [1, 2, 3]:
    print('\033[1;31mNúmero inválido 😢\033[m')  # Vermelho
else:
    # Jogada do computador
    num_computador = randint(1, 3)
    
    # Mostrando escolhas
    print(f'\nVocê escolheu: \033[1;32m{opcoes[num_jogador-1]} {emojis[num_jogador-1]}\033[m')  # Verde
    print(f'Computador escolheu: \033[1;31m{opcoes[num_computador-1]} {emojis[num_computador-1]}\033[m\n')  # Vermelho
    
    # Decisão do jogo
    if num_jogador == num_computador:
        print('\033[1;33mOpa, deu empate! 🤝\033[m')  # Amarelo
    elif (num_jogador == 1 and num_computador == 3) or \
         (num_jogador == 2 and num_computador == 1) or \
         (num_jogador == 3 and num_computador == 2):
        print('\033[1;32mParabéns, você ganhou! 🎉\033[m')  # Verde
    else:
        print('\033[1;31mVocê perdeu 😢\033[m')  # Vermelho
