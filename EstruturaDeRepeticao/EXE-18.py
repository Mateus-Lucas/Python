# 18 - Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.

quantidade = int(input('informe a quantidade de termos que você quer na lista: '))
lista = []
termos = 0
numero = 0

while True:
    if termos != quantidade:
        numero = int(input('informe um número para lista: '))
        lista.append(numero) 
        termos = len(lista)
        print(lista)
    else:
        break


soma = sum(lista)
menor = min(lista)
maior = max(lista)

print(f'Maior valor da lista: {maior}')
print(f'Menor valor da lista: {menor}')
print(f'Soma de todos os valores: {soma}')