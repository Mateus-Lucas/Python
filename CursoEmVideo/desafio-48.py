print('\033[1;34m' + '=' * 20, '| Desafio 48 |', '=' * 20 + '\033[m')

'''
🔥 Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram no intervalo de 1 até 500 🔥
'''

soma = 0
cont = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i

print(f'\033[1;32mA soma de todos os {cont} valores solicitados é {soma}\033[m')
