print('\033[1;33m' + '=' * 20 + ' | Desafio 95 | ' + '=' * 20 + '\033[m')

''' Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de 
visualização de detalhes de aproveitamento de cada jogador'''

jogadores = []

while True:
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


    # Guardando cada jogador numa lista 
    jogadores.append(jogador.copy())

    # Verificando se o usuário quer continuar
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite apenas S ou N, Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 30)

# Exibindo cabeçalho
print(f'{"cod":<5}', end='')
for k in jogadores[0].keys():
     print(f'{k:<15}', end='')
print('\n','-' * 35)

# Exibindo jogadores e seus dados
cont = 0
for j in jogadores:
        print(f'{cont:<5}', end='')
        print(f'{j["nome"]:<15}', end='')
        print(f'{str(j["gols"]):<15}', end='')
        print(f'{j["total"]:<15}')
        cont += 1
print('\n','-' * 35)

# Mostrando dados de um jogador específico
cod_jogador = 0
while cod_jogador != 999:
    cod_jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod_jogador == 999:
        print('-- Volte Sempre --')
        break
    if cod_jogador < 0 or cod_jogador >= len(jogadores) :
        print(f'ERRO! Não existe jogador com código {cod_jogador}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[cod_jogador]["nome"]}')
        for c, g in enumerate(jogadores[cod_jogador]['gols']):
            print(f'      No jogo {c+1} fez {g} gols')
    print('\n','-' * 35)
                

# # EXERCICIO GUANABARA                
# time = list()
# jogador = dict()
# partidas = list()

# while True:
#     jogador.clear()
#     jogador['nome'] = str(input('Nome do jogador: '))
#     tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#     partidas.clear()
#     for c in range(0, tot):
#         partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     time.append(jogador.copy())
#     while True:
#         resp = str(input('Quer continuar? [S/N] ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('ERRO! Responda apenas S ou N.')
#     if resp == 'N':
#         break
# print('-=' * 30)
# print('cod ', end='')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
# print('-' * 40)
# for k, v in enumerate(time):
#     print(f'{k:>3} ', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-' * 40)
# while True:
#     busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
#     if busca == 999:
#         break
#     if busca >= len(time):
#         print(f'ERRO! Não existe jogador com código {busca}')
#     else:
#         print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
#         for i, g in enumerate(time[busca]['gols']):
#             print(f'     No jogo {i+1} fez {g} gols.')
#     print('-' * 40)
# print('<< VOLTE SEMPRE >>')