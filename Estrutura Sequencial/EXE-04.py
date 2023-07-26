#04 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#definição das variaveis
nota1 = float(input('Digite a nota da 1° bimestre: '))
nota2 = float(input('Digite a nota da 2° bimestre: '))
nota3 = float(input('Digite a nota da 3° bimestre: '))
nota4 = float(input('Digite a nota da 4° bimestre: '))

#calculo para média
media = (nota1+nota2+nota3+nota4)/4

#exibindo média 
print(f'A média das notas é {media}')