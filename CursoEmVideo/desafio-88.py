print('\033[1;33m' + '=' * 20 + ' | Desafio 88 | ' + '=' * 20 + '\033[m')

''' Faça um programa que ajude um jogador da MEGA SENHA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta'''

print(f'-' * 50)
print(f'JOGO DA MEGA SENA')
print(f'-' * 50)

from random import randint
from time import sleep

print('\033[36m' + '-' * 50 + '\033[m')  # ⭐ ALTEREI AQUI → cor ciano
print('\033[1m        🎰 JOGO DA MEGA SENA 🎰        \033[m')  # ⭐ ALTEREI AQUI → título centralizado
print('\033[36m' + '-' * 50 + '\033[m')

from random import randint
from time import sleep

num_jogos = int(input('\033[33mQuantos jogos serão gerados? \033[m'))

jogos = []  # Lista principal
jogo = []   # Lista complementar

print('\n\033[35m⏳ Aguarde enquanto os jogos estão sendo gerados...\033[m\n')  

# Looping que repete a quantidade de vezes que o jogador quer
for js in range(num_jogos):
    # Utilizando While ao invés do for para não repetir números
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:  # evita repetição
            jogo.append(num)
    jogo.sort()  # Ordendando valores da mega sena
    sleep(1) 
    print(f'\033[32mJogo {js+1:02d}: {jogo}\033[m')
    jogos.append(jogo[:])
    jogo.clear()

print('\n\033[1;34m' + '=' * 50 + '\033[m')
print('\033[1;34m✨ BOA SORTE NOS SEUS JOGOS! ✨\033[m')
print('\033[1;34m' + '=' * 50 + '\033[m')

# EXERCICIO GUANABARA
# lista = []
# jogos = []
# print('-' * 30)
# print('      JONA NA MEGA SENA      ')
# print('-' * 30)
# quant = int(input('Quantos jogos você quer que eu sorteie: '))
# tot = 0
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print('-=' * 3, f'SORTENADO {quant} JOGOS', '-=' * 3)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i}: {l}')
#     sleep(2)
