print('=' * 20, '| Desafio 38 |', '=' * 20)

"""
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
 - O primeiro valor é maior
 - O segundo valor é maior
 - Não existe valor maior, os dois são iguais
"""

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
mensagem = ''
moldura = ''

# Define a mensagem a ser exibida de acordo com o comparativo dos números e guarda na varíavel "mensagem"
# Muda também a moldura para exibir o resultado de acordo com a mensagem a ser exibida
if n1 > n2:
    mensagem = '\033[1;32mO primeiro valor é maior.\033[m'
    moldura = '-=' * 13
elif n2 > n1:
    mensagem = '\033[1;31mO segundo valor é maior.\033[m'
    moldura = '-=' * 13
else:
    mensagem = '\033[1;33mNão existe valor maior, os dois são iguais.\033[m'
    moldura = '-=' * 22

# Exibe moldura e mensagem com consistência
print(moldura)
print(mensagem)
print(moldura)
