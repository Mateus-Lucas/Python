# 01 - Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = 0

while True: # Repetição vai ser verdadeira até chegar no break
    nota = float(input('Informe uma nota entre 0 e 10: '))
    
    if 0 <= nota <= 10:
        break  # Sai do loop se a nota for válida
    else:
        print('Valor inválido. A nota deve estar entre 0 e 10.')


