print('=' * 20, '| Desafio 53 |', '=' * 20)

"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
"""

# Lê a frase e normaliza (sem espaços extras e em maiúsculas)
frase = input("Digite uma frase: ").strip().upper()

# Remove todos os espaços da frase
junto = frase.replace(" ", "")

# Gera a versão invertida da frase com slicing
inverso = junto[::-1]

# Verifica se é um palíndromo
if junto == inverso:
    print(f"A frase '{frase}' É um palíndromo! ({junto} = {inverso})")
else:
    print(f"A frase '{frase}' NÃO é um palíndromo. ({junto} ≠ {inverso})")
