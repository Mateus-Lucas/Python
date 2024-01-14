# 20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
# limitando o fatorial a números inteiros positivos e menores que 16.

resultado = 0
continuar = 's'
num = 0

# Função para calcular o fatorial de um número usando looping
def fatorial_loop(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

while True:
    num = int(input('Informe o valor que você deseja calcular o fatorial: '))
    
    if 0 <= num <= 16:
        # Calcular e exibir o fatorial
        resultado = fatorial_loop(num)
        print('O fatorial de', num, 'é:', resultado)
    
        # Continua o looping caso queira
        continuar = input('Quer continuar? Digite "s" para sim, ou "n" para não: ')
        if continuar.lower() != 's':
            break
    else:
        print('Apenas números entre 0 e 16 são permitidos')



