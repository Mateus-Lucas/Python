print('\033[1;33m' + '=' * 20, '| Desafio 72 |', '=' * 20 + '\033[m')

''' Crie um programa que tenha uma tupla totalmente preenchida com contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso'''

# Tupla com o conjunto de números por extenso
numeros_extenso = (
    'zero', 
    'um', 
    'dois', 
    'três', 
    'quatro', 
    'cinco', 
    'seis', 
    'sete', 
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte'
)

numero = 0
continuar = 'S'

# Looping que verifica se o usuário quer continuar
while True:
    if continuar == 'S':
        # Looping que verifica se o usuário está digitando o número entre 0 e 20
        while True:
            numero = int(input('Informe um número entre 0 e 20: '))
            if numero < 0 or numero > 20:
                print('Por favor, informe um número entre 0 e 20!')
            else:
                break

        # Puxando índice da tupla equivalente ao número digitado
        print(f'O número {numero} por extenso é {numeros_extenso[numero]}')
        continuar = str(input('Você quer continuar? S para sim e N para não: ')).strip().upper()
        continuar = continuar[0]
    elif continuar == 'N':
        break
    else:
        print('Você digitou errado. ', end='')
        continuar = str(input('Você quer continuar? S para sim e N para não: ')).strip().upper()
        continuar = continuar[0]
print('--- FIM DO PROGRAMA ---')