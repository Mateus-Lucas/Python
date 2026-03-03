print('\033[1;33m' + '=' * 20 + ' | Desafio 101 | ' + '=' * 20 + '\033[m')

''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATÓRIO'''

# CÓDIGO GUANABARA 
# def voto(ano):
#     # Importação local
#     from datetime import date
#     atual = date.today().year
#     idade = atual - ano
#     if idade < 16:
#         return f'Com {idade} anos: NÃO VOTA'
#     elif 16 <= idade < 18 or idade > 65:
#         return f'Com {idade} anos: VOTO OPCIONAL'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO'

# # CÓDIGO PRINCIPAL
# nasc = int(input('Em que ano você nasceu? '))
# print(voto(nasc))


# CÓDIGO PESSOAL
def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade >= 18:
        return f'obrigatório!'
    elif idade >= 16:
        return f'opcional!'
    else:
        return f'negado!'


# # Programa principal
ano_nascimento = int(input('Informe seu ano de nascimento: '))
print(f'Seu voto é {voto(ano_nascimento)}')