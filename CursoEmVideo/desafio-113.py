print('\033[1;33m' + '=' * 20 + ' | Desafio 113 | ' + '=' * 20 + '\033[m')

''' Reescreva a função leiaInt() que fizemos no desfaio 104, incluindo agora
a possibilidade de digitação de um número de tipo inválido. aproveite e crie 
também uma função leiaFloat() com a mesma funcionalidade.'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):  # Correção aqui (vírgula em vez de or)
            print('\033[1;31mERRO: por favor digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):  # Correção aqui (vírgula em vez de or)
            print('\033[1;31mERRO: Por favor digite um número decimal válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0  # Correção aqui para evitar o loop infinito no Ctrl+C
        else:
            return n
        

n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor decimal: ')
print(f'O valor inteiro digitado foi {n1} e o decimal foi {n2}')