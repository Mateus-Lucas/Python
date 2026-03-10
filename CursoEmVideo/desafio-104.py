print('\033[1;33m' + '=' * 20 + ' | Desafio 104 | ' + '=' * 20 + '\033[m')

''' Crie um programa que tenha função leiaInt(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo a 
validação para aceitar apenas um valor númerico.
Ex: n = leiaInt('Digite um número')'''

def leiaInt(mensagem):
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
    return numero


# PROGRAMA PRINCIPAL
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')