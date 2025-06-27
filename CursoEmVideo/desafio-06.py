print('='*11,'| DESAFIO 06 |', '='*11)
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Informe um número: "))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'A raiz quadrada de {numero} é {raiz_quadrada:.2f}')