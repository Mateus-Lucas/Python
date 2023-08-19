# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# h = altura

h = float(input('Informe a altura: '))

print('Informe seu gênero: ')
print('1 - Homem')
print('2 - Mulher')

genero = int(input('Irforme a opção desejada: '))

if genero == 1:
    peso_ideal = (72.7*h) - 58
    print(f'Seu peso ideal é aproximadamente: {peso_ideal:.0f}kg')

elif genero == 2:
    peso_ideal = (62.1*h) - 44.7
    print(f'Seu peso ideal é aproximadamente: {peso_ideal:.0f}kg')
else:
    print('opção inválida')




