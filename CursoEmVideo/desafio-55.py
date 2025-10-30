print('=' * 20, '| Desafio 55 |' ,'=' * 20)

''' Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos '''

pesos = []

for i in range(1, 6):
    peso = float(input(f'{i}ª pessoa, por favor informe seu peso: '))
    pesos.append(peso)  # adiciona o peso na lista

print(f'\nOs pesos informados foram: {pesos}')
print(f'O maior peso é \033[1;33m{max(pesos)} Kg\033[m')
print(f'O menor peso é \033[1;33m{min(pesos)} Kg\033[m')