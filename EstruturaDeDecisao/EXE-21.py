# # 21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
# # depois informar quantas notas de cada valor serão fornecidas. 
# # As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# # O valor mínimo é de 10 reais e o máximo de 600 reais. 
# # O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# # Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, 
# # uma nota de 5 e uma nota de 1;
# # Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, 
# # quatro notas de 10, uma nota de 5 e quatro notas de 1.

print('---| Bem vindo ao caixa eletrônico |----')
print('Valor mínimo para saque: 10 reais') 

saque = int(input('Informe o valor do saque: '))

if 10 <= saque <= 999:
    notas_100 = saque // 100
    saque %= 100

    notas_50 = saque // 50
    saque %= 50

    notas_10 = saque // 10
    saque %= 10

    notas_5 = saque // 5
    saque %= 5

    notas_1 = saque

    def imprimir_notas(qtd, valor):
        if qtd > 0:
            if qtd > 1:
                print(f'{qtd} cédulas de {valor}')
            else:
                print(f'{qtd} cédula de {valor}')

    imprimir_notas(notas_100, 100)
    imprimir_notas(notas_50, 50)
    imprimir_notas(notas_10, 10)
    imprimir_notas(notas_5, 5)
    imprimir_notas(notas_1, 1)
else:
    print('Valor de saque inválido. O valor mínimo é 10 reais e o máximo é 999 reais.')



