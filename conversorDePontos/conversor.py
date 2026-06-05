import requests
import os
from datetime import datetime

PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
PASTA_DADOS = os.path.join(PASTA_PROJETO, 'dados')

os.makedirs(PASTA_DADOS, exist_ok=True)

ARQUIVO = os.path.join(PASTA_DADOS, 'historico.txt')

def titulo(texto):
    print('=' * 40)
    print(texto.center(40))
    print('=' * 40)


def cotacao_dolar():
    try:
        url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()
        return float(dados['USDBRL']['bid'])

    except Exception as erro:
        print(f'\nErro ao obter cotação: {erro}')
        print('Utilizando cotação padrão de R$ 5.50')
        return 5.50


def leia_float(msg):
    while True:
        try:
            return float(input(msg).replace(',', '.'))
        except ValueError:
            print('ERRO: Digite um número válido.')


def leia_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('ERRO: Digite um número inteiro válido.')


def registrar_ganhos():
    titulo('REGISTRAR GANHOS')

    dolar = cotacao_dolar()

    print(f'\nCotação atual: R$ {dolar:.4f}')

    print('\n--- VALORES DO DIA ---')

    prime = leia_int('Prime Opinion: ')
    toluna = leia_int('Toluna: ')
    ysense = leia_float('ySense (US$): ')

    prime_convertido = (prime / 100) * dolar
    toluna_convertido = toluna / 1360
    ysense_convertido = ysense * dolar

    total = prime_convertido + toluna_convertido + ysense_convertido

    meta = leia_float('\nMeta do dia (R$): ')

    print(f'''
{'=' * 40}
RESULTADO
{'=' * 40}
Prime Opinion: R$ {prime_convertido:.2f}
Toluna:        R$ {toluna_convertido:.2f}
ySense:        R$ {ysense_convertido:.2f}
----------------------------------------
Total:         R$ {total:.2f}
''')

    if total >= meta:
        print(f'✅ Meta batida! Sobrou R$ {total - meta:.2f}')
    else:
        print(f'❌ Faltam R$ {meta - total:.2f}')

    salvar = input('\nDeseja salvar este resultado? [S/N] ').strip().upper()

    if salvar == 'S':
        os.makedirs('dados', exist_ok=True)

        data = datetime.now().strftime('%d/%m/%Y %H:%M')

        with open(ARQUIVO, 'a', encoding='utf-8') as arquivo:
            arquivo.write(
                f'{data} | '
                f'Prime: {prime_convertido:.2f} | '
                f'Toluna: {toluna_convertido:.2f} | '
                f'ySense: {ysense_convertido:.2f} | '
                f'Total: {total:.2f}\n'
            )

        print('✅ Resultado salvo com sucesso!')
    else:
        print('⚠️ Resultado não salvo.')


def ver_historico():
    titulo('HISTÓRICO')

    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

            if conteudo.strip():
                print(conteudo)
            else:
                print('Histórico vazio.')

    except FileNotFoundError:
        print('Nenhum histórico encontrado.')


def total_acumulado():
    titulo('TOTAL ACUMULADO')

    soma = 0

    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split('|')
                total = float(partes[-1].replace('Total:', '').strip())
                soma += total

        print(f'Total acumulado: R$ {soma:.2f}')

    except FileNotFoundError:
        print('Nenhum histórico encontrado.')

    except Exception as erro:
        print(f'Erro ao calcular total: {erro}')


def limpar_historico():
    titulo('LIMPAR HISTÓRICO')

    confirmar = input(
        'Tem certeza que deseja apagar todo o histórico? [S/N] '
    ).strip().upper()

    if confirmar == 'S':
        try:
            open(ARQUIVO, 'w', encoding='utf-8').close()
            print('✅ Histórico apagado.')
        except FileNotFoundError:
            print('Nenhum histórico encontrado.')
    else:
        print('Operação cancelada.')


while True:
    titulo('GERENCIADOR DE GANHOS')

    print('[1] Registrar ganhos')
    print('[2] Ver histórico')
    print('[3] Ver total acumulado')
    print('[4] Limpar histórico')
    print('[5] Sair')

    opcao = input('\nEscolha uma opção: ').strip()

    if opcao == '1':
        registrar_ganhos()

    elif opcao == '2':
        ver_historico()

    elif opcao == '3':
        total_acumulado()

    elif opcao == '4':
        limpar_historico()

    elif opcao == '5':
        print('\nEncerrando sistema...')
        break

    else:
        print('\nOpção inválida.')

    input('\nPressione ENTER para continuar...')