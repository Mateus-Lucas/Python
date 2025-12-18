print('\033[1;33m' + '=' * 20, '| Desafio 73 |', '=' * 20 + '\033[m')

''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
a) Os 5 primeiros. 
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Internacional.'''

def linha():
    print('\033[1;35m=\033[m' * 60)

brasileirao = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 
               'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Bragantino',
               'Atlético-MG', 'Santos', 'Corinthians', 'Vasco da Gama', 'EC Vitória',
               'Internacional', 'Ceará SC', 'Fortaleza', 'Juventude', 'Sport Recife')

print(f'Lista de times: {brasileirao}')
linha()
print(f'Os 5 primeiro times classificados são {brasileirao[:5]}')
linha()
print(f'Os 4 últimos colocados são {brasileirao[-4:]}')
linha()
print(f'Times em ordem alfabética {sorted(brasileirao)}')
linha()

# Index 15, por isso é adicionado mais 1.
posicao = brasileirao.index('Internacional') + 1
print(f'O Internacional ficou em {posicao}° lugar')

# cont = 0

# # Looping para listar todos os times de forma separada e para quando achar um chamado "Internacional"
# for t in brasileirao:
#     cont += 1
#     if t == 'Internacional':
#         break

# # Colocado o contador -1 pois o índice é diferente da posição dos times, começa com 0
# print(f'O Internacional ficou em {cont}° lugar')