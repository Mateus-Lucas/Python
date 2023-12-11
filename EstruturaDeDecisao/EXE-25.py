# 25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print('-----------| Interrogatório |------------ \n Responda as perguntas com s \n s para sim \n n para não \n' )

telefone = input('Telefonou para a vítima? ')
estar = input('Esteve no local do crime? ')
morar = input('Mora perto da vítima? ')
dever = input('Devia para a vítima? ')
trabalhar = input('Já trabalhou com a vítima? ')

chance_culpa = 0

if all(resposta.lower() in ['s', 'n'] for resposta in [telefone, estar, morar, dever, trabalhar]):
    if telefone == 's':
        chance_culpa += 1
    if estar == 's':
        chance_culpa += 1
    if morar == 's':
        chance_culpa += 1
    if dever == 's':
        chance_culpa += 1
    if trabalhar == 's':
        chance_culpa += 1

    classificacao = ''

    if 0 <= chance_culpa < 2:
        classificacao = 'Inocente' 
    elif chance_culpa == 2:
        classificacao = 'Suspeito' 
    elif chance_culpa == 5:
        classificacao = 'Assassino' 
    else:
        classificacao = 'Cúmplice' 

    if chance_culpa == 1:
        print(f'\n Você é {classificacao} com {chance_culpa} ponto de classificação')
    else:
        print(f'\n Você é {classificacao} com {chance_culpa} pontos de classificação')

else:
   print('\n Diga apenas sim ou não')

