print('\033[1;33m' + '=' * 20 + ' | Desafio 103 | ' + '=' * 20 + '\033[m')

''' Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador.
mesmo que algum dado não sido informado corretamente'''

# CÓDIGO GUANABARA
# def ficha(jog='<desconhecido>', gol=0):
#     print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


# # PROGRAMA PRINCIPAL
# n = str(input('Nome do jogador: '))
# g = str(input('Número de gols: '))
# if g.isnumeric():
#     g = int(g)
# else: g = 0
# if n.strip() == '':
#     ficha(gol=g)
# else:
#     ficha(n, g)

# # CÓDIGO PESSOAL
def ficha(nome='<desconhecido>', gols=0):
    # Trata o nome se ele vier vazio ou só com espaços
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s).'

# PROGRAMA PRINCIPAL
n = str(input('Nome: '))
g = str(input('Gols: '))

# Validação rápida de gols
g = int(g) if g.isnumeric() else 0

print(ficha(n, g))
