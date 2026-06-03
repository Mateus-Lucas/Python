from lib.interface import *
from solucao.cores import *

while True:
    resposta = menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova Pessoa',
        'Sair do Sistema'
    ])

    if resposta == 1:
        cabecalho(cor_azul('PESSOAS CADASTRADAS'))

    elif resposta == 2:
        cabecalho(cor_verde('NOVO CADASTRO'))

    elif resposta == 3:
        cabecalho(cor_amarelo('ENCERRANDO SISTEMA'))
        print(cor_vermelho('Saindo do sistema... Até logo!'))
        break

    else:
        print(cor_vermelho('ERRO! Digite uma opção válida!'))