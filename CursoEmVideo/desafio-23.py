print('=' * 11, '| DESAFIO 23 |', '=' * 11)

"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos seprados.
Ex:
Digite um número: 1834
unidade: 4 dezena:3 centena:8 mlhar:1
"""

def separar_digitos(numero: int):
    if not (0 <= numero <= 9999):
        print("Valor inválido! Digite um número entre 0 e 9999.")
        return

    # Preenche com zeros à esquerda para sempre ter 4 caracteres
    numero_str = str(numero).zfill(4)

    nomes = ["Milhar", "Centena", "Dezena", "Unidade"]

    for nome, digito in zip(nomes, numero_str):
        print(f"{nome}: {digito}")

# --- Programa principal ---
try:
    numero = int(input("Informe um número de 0 a 9999: "))
    separar_digitos(numero)
except ValueError:
    print("Entrada inválida! Digite apenas números inteiros.")


# CÓDIGO GUANABARA 

# numero = int(input('Informe um número de 0 a 9999: '))

# unidade =  numero    // 1 % 10
# dezena  =  numero   // 10 % 10
# centena =  numero  // 100 % 10
# milhar  =  numero // 1000 % 10
# print(f'Unidade: {unidade}')
# print(f'Dezena: {dezena}')
# print(f'Centena: {centena}')
# print(f'Milhar: {milhar}')



""" #CÓDIGO PESSOAL# 

numero_str = str(numero)
contagem_digitos = len(numero_str)
unidade = 0
dezena = 0
centena = 0
milhar = 0

if contagem_digitos <= 4:
    if contagem_digitos == 4:
        unidade = numero_str[3]
        dezena = numero_str[2]
        centena = numero_str[1]
        milhar = numero_str[0]
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')
    if contagem_digitos == 3:
        unidade = numero_str[2]
        dezena = numero_str[1]
        centena = numero_str[0]
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')
    if contagem_digitos == 2:
        unidade = numero_str[1]
        dezena = numero_str[0]
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')
    if contagem_digitos == 1:
        unidade = numero_str[0]
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')
else:
    print('Valor inválido')

"""