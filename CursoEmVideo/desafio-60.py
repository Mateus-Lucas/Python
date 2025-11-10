print('=' * 20, '| Desafio 60 |' ,'=' * 20)

'''
🧮 Desafio 60
Faça um programa que leia um número e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

# Solicita ao usuário um número para calcular o fatorial
num = int(input('\nDigite um número para calcular o fatorial: '))

# Inicializa as variáveis
contador = num
resultado = 1

# Exibe o título do cálculo
print(f'\nCalculando {num}! = ', end='')

# Loop para multiplicar todos os números de 'num' até 1
while contador > 0:
    print(f'{contador}', end=' ')
    print('x ' if contador > 1 else '= ', end='')  # Mostra o formato "5 x 4 x 3 x ... ="
    resultado *= contador  # Multiplica o resultado pelo contador atual
    contador -= 1          # Diminui o contador até chegar em 1

# Exibe o resultado final formatado
print(f'{resultado}\n')

print('=' * 55)
print('🎯 Cálculo concluído com sucesso!')
print('=' * 55)
