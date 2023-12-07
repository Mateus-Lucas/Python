# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))

if numero2 == 0:
    print('Erro: Divisão por zero.')
else:
    resultado = 0

    print('\n Adição = + \n Subtração = - \n Multiplicação = x \n Divisão = / ')
    operacao = input('\n Qual operação você deseja fazer com esses números: ')

    if operacao in ['+', '-', 'x', '/']:
        if operacao == '+':
            resultado = numero1 + numero2
            print('Somando números..')
        elif operacao == '-':
            resultado = numero1 - numero2
            print('Subtraindo números...')
        elif operacao == 'x':
            resultado = numero1 * numero2
            print('Multiplicando números...')
        else:
            resultado = numero1 / numero2
            print('Dividindo números...')

        resultado_arredondado = round(resultado, 0)

        par = resultado % 2 == 0
        positivo = resultado >= 0
        inteiro = resultado == resultado_arredondado
        decimal = not inteiro

        print(f'\n Atributos do número: {resultado}')
        if par:
            print(' Par')
        else:
            print(' Ímpar')

        if positivo:
            print(' Positivo')
        else:
            print(' Negativo')

        if inteiro:
            print(' Inteiro')
        else:
            print(' Decimal')
    else:
        print('Operação inválida')

print('Programa concluído.')

  
  