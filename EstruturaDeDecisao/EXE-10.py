# 10 - Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno_estudante = input('Informe o turno que você estuda M-matutino ou V-Vespertino ou N- Noturno: ')

if turno_estudante == 'M':
    print('Bom dia')
elif turno_estudante == 'V':
    print('Boa tarde')
elif turno_estudante == 'N':
    print('Boa noite')
else:
    print('Valor inválido')