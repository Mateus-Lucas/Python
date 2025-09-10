print('=' * 11, '| DESAFIO 27 |', '=' * 11)

"""
  Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
  escolhido pelo computador

  O programa deverá escrever na tela se o usuário venceu ou perdeu
"""

from random import randint
from time import sleep

print('-=-' * 20)
print('Jogo da advinhação. Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

n1 = randint(0, 5) #Gerando um número aleatório entre 0 e 5
n2 = int(input('Informe um número entre 0 e 5: '))

print('-=-' * 20) 
print('PROCESSANDO...') #Simulando pensamento do computador
sleep(3)
print('-=-' * 20)

if 0 <= n2 <= 5: #Vericando se o usuário digitou um número entre 0 e 5
    if n1 == n2: #Vericando se o número digitado pelo usuário é igual ao gerado em n1 
        print('PARABÉNS, você acertou o número que eu estava pensando!!!')
    else:
        print('Você errou, tente novamente!')
else:
    print('Por favor, insira valores entre 0 e 5!')
