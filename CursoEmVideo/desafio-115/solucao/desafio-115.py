print('\033[1;33m' + '=' * 20 + ' | Desafio 115 | ' + '=' * 20 + '\033[m')

''' Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo
seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções:
cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

import cores
import erros
import alternativas

print('\033[1;33m' + '=' * 20 +
      ' | Desafio 115 | ' +
      '=' * 20 + '\033[m')

while True:

    print('-' * 30)
    print('MENU PRINCIPAL')
    print('-' * 30)

    print(f'{cores.cor_amarelo("1")} - {cores.cor_azul("Ver pessoas cadastradas")}')
    print(f'{cores.cor_amarelo("2")} - {cores.cor_azul("Cadastrar nova pessoa")}')
    print(f'{cores.cor_amarelo("3")} - {cores.cor_azul("Sair do sistema")}')

    opcao = erros.tratamento_erro(
        cores.cor_amarelo('Sua opção: ')
    )

    if opcao == 1:
        alternativas.listar_pessoas()

    elif opcao == 2:
        alternativas.cadastrar_pessoa()

    elif opcao == 3:
        alternativas.sair()
        break