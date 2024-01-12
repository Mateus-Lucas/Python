# 17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# Função para calcular o fatorial de um número usando looping
def fatorial_loop(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

# Solicitar o valor ao usuário
num = int(input('Informe o valor que você deseja calcular o fatorial: '))

# Calcular e exibir o fatorial
resultado = fatorial_loop(num)
print('O fatorial de', num, 'é:', resultado)