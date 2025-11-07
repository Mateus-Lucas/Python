print('=' * 20, '| Desafio 58 |', '=' * 20)

"""
Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 a 10. 
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint
from time import sleep

print('-=-' * 20)
print('\033[1;33mJogo da adivinhação!\033[m')
print('Vou pensar em um número entre 0 e 10... Tente adivinhar!')
print('-=-' * 20)

n1 = randint(0, 10)  # Número gerado pelo computador
contador = 0
acertou = False

while not acertou:
    n2 = int(input('\nQual o seu chute? '))
    contador += 1
    print('-' * 20)
    print('PROCESSANDO...')
    print('-' * 20)
    sleep(1)

    if n2 == n1:
        acertou = True
    else:
        print('\033[1;31mVocê errou!\033[m Tente novamente.')

print('\n\033[1;32mParabéns! Você adivinhou o número!\033[m')
print(f'\033[1;33mForam necessárias {contador} tentativas para acertar o número {n1}.\033[m')
