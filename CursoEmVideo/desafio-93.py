print('\033[1;33m' + '=' * 20 + ' | Desafio 93 | ' + '=' * 20 + '\033[m')

'''
Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos 
em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
'''

# Criando dicionário do jogador
jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))

# Número de partidas
partidas = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))

gols = []

# Leitura de gols por partida
for c in range(1, partidas + 1):
    gols.append(int(input(f'   Quantos gols na partida {c}? ')))

# Salvando no dicionário
jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)

# Exibindo campos do dicionário
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

# Detalhamento das partidas
print('-=' * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas")
for c, v in enumerate(jogador['gols']):
    print(f' => Na partida {c + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
