# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

dia_semana = int(input('Digite um número de 1 a 7 para os dias da semanas (1-Domingo, 2- Segunda, etc.): '))

if 1 <= dia_semana <= 7:
    if dia_semana == 1:
       dia = 'Domingo'
    elif dia_semana == 2:
       dia = 'Segunda'
    elif dia_semana == 3:
       dia = 'Terça'
    elif dia_semana == 4:
       dia = 'Quarta'
    elif dia_semana == 5:
       dia = 'Quinta'
    elif dia_semana == 6:
       dia = 'Sexta'
    elif dia_semana == 7:
       dia = 'Sábado'
    print(f'O dia da semana é {dia}')
else:
    print('Dia inválido')
