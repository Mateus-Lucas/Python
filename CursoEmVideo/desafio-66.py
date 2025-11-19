print('\033[1;33m' + '=' * 20, '| Desafio 66 |' , '=' * 20 + '\033[m')

'''
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

contador = 0   # Conta quantos números válidos foram digitados
soma = 0       # Soma dos números

while True:
    n = int(input('Digite um valor: '))
    if n == 999:  # Condição de parada
        break
    contador += 1    # Contador aumenta
    soma += n        # Soma acumulada

print(f'\nForam digitados {contador} números')
print(f'A soma desses números é {soma}')
