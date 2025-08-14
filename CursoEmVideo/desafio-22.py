print('=' * 11, '| DESAFIO 22 |', '=' * 11)

"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas e minúsculas.
    - Quantas letras ao todo (sem considerar espaços).
    - Quantas letras tem o primeiro nome.
"""

# Entrada de dados
nome = input('Informe seu nome completo: ').strip()

# Processamento
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
quant_letras = len(nome.replace(' ', ''))  # Remove espaços antes de contar
letras_primeiro_nome = len(nome.split()[0])  # Conta letras do primeiro nome

# Saída formatada
print(f'\nNome todo em MAIÚSCULO: {nome_maiusculo}')
print(f'Nome todo em minúsculo: {nome_minusculo}')
print(f'Quantidade de letras (sem espaços): {quant_letras}')
print(f'Quantidade de letras no primeiro nome: {letras_primeiro_nome}')
