#07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

#definição de variavel
lado = float(input('Digite em cm o lado do quadrado: '))

#calculos
area = lado**2
dobro_area = area*2

#exibindo resultados
print(f'A área desse quadrado é: {area:.2f}')
print(f'O dobro da área desse quadrado é: {dobro_area:.2f}')