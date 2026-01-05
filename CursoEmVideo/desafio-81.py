print('\033[1;33m' + '=' * 20, '| Desafio 81 |', '=' * 20 + '\033[m')

''' Crie um programa que leia vários números e colocar em uma lista. Depois disso moste: 
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista'''

lista = []

# Looping para pedir os valores para o usuário colocar na lista
while True:
    numero = int(input('Informe um número: '))
    lista.append(numero)
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

    # Verificando de o usuário está digitando sim ou não
    while continuar not in 'SN':
        print('Por favor digite apenas Sim ou Não [S/N]!')
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

    # Para o programa de o usuário digitar não
    if continuar == 'N':
        break


print(f'Foram digitados {len(lista)} números')
# Invertendo a lista
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')

# Verificando se tem o número 5 na lista
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
