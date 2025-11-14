print('\033[1;33m' + '=' * 20, '| Desafio 65 |' , '=' * 20 + '\033[m')

'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

# Lista onde os números serão armazenados
numeros = []

# Função para facilitar separadores visuais
def linha():
    print('\033[1;34m' + '-' * 40 + '\033[m')

print('\n\033[1;36mDigite números inteiros. Para parar, escolha "n" quando perguntado.\033[m\n')

while True:
    # Entrada do número
    n = int(input('\033[1;32mInforme um número inteiro: \033[m'))
    numeros.append(n)
    linha()

    # Pergunta se deseja continuar
    resposta = str(input('\033[1;35mQuer continuar [s/n]? \033[m')).strip().lower()
    linha()

    # Validação opcional (deixa o programa mais robusto)
    while resposta not in ('s', 'n'):
        print('\033[1;31mOpção inválida! Digite apenas "s" ou "n".\033[m')
        resposta = str(input('\033[1;35mQuer continuar [s/n]? \033[m')).strip().lower()
        linha()

    if resposta == 'n':
        break

# Cálculos finais
c = len(numeros)            # quantidade
media = sum(numeros) / c    # média
maior = max(numeros)        # maior valor
menor = min(numeros)        # menor valor

# Resultado estilizado
print('\n\033[1;33mRESULTADO FINAL\033[m')
linha()
print(f'Você digitou \033[1;33m{c}\033[m números.')
print(f'A média dos valores é \033[1;33m{media:.2f}\033[m.')
print(f'O maior número foi \033[1;32m{maior}\033[m e o menor foi \033[1;31m{menor}\033[m.')
linha()
print('\033[1;32mPrograma finalizado.\033[m')
