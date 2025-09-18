print('=' * 11, '| Desafio 31 |' ,'=' * 11)

'''
 Desenvolva um programa que pergunte a distância de uma viagem em Km. 
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longes
'''

distancia = float(input('Informe a distância da viagem em Km: '))

if distancia <= 200: #Estrutura condicional que muda o preço da passagem de acordo com a distância
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45

# passagem = distancia * 0.5 if distancia <= 200 else distancia * 0.45 ( Outra forma de fazer com if simplificado )

print(f'A valor da passagem é R${passagem:.2f}')



