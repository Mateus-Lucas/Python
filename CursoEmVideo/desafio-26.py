print('=' * 11, '| DESAFIO 26 |', '=' * 11)

"""
Faça um programa que leia uma frase pelo teclado e mostre:
  Quantas vezes aparece a letra "A".
  Em que posição ela aparece a primeira vez.
  Em que posição ela aparece a última vez
"""

frase = str(input('Fale uma frase: ')).strip()

frase = frase.upper()
letras_a = frase.count('A')
primeira_a = frase.find('A') + 1
ultima_a = frase.rfind('A') + 1

print(f'A letra A aparece {letras_a} vezes na frase')
print(f'A primeira posição da letra A foi {primeira_a}')
print(f'A última posição da letra A foi {ultima_a}')
