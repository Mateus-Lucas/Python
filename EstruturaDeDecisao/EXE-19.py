# 19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com:
# 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input('Informe um número inteiro menor que 1000: '))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

def formatar_quantidade(valor, singular, plural):
    if valor == 1:
        return f'{valor} {singular}'
    elif valor > 1:
        return f'{valor} {plural}'
    else:
        return ''

saida = ''
saida += formatar_quantidade(centena, 'centena', 'centenas')
saida += ', ' if centena and (dezena or unidade) else ''
saida += formatar_quantidade(dezena, 'dezena', 'dezenas')
saida += ' e ' if dezena and unidade else ''
saida += formatar_quantidade(unidade, 'unidade', 'unidades')

print(f'{numero} = {saida}')

