# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes 
# situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer 
# pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input('Informe o valor de a em ax2 + bx + c: '))

if a == 0:
    print('Equação não é do segundo grau, programa encerrado')
else: 
    b = int(input('Informe o valor de b em ax2 + bx + c: '))
    c = int(input('Informe o valor de c em ax2 + bx + c: '))
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('A equação não possui raízes, programa encerrado')
    elif delta == 0:
        x = -b / (2*a)
        print(delta)
        print(f'A equação possui uma raiz real igual a {x}')
    else: 
        x1 = (-b + (delta**(1/2)))/(2*a)
        x2 = (-b - (delta**(1/2)))/(2*a)
        print(f'A equação possui duas raizes reais iguais a {x1} e {x2}')
    