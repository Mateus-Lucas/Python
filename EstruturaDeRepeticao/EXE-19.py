# 19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

# Váriaveis iniciais
quantidade = int(input('informe a quantidade de termos que você quer na lista: '))
lista = []
termos = 0
numero = 0

# Looping para pedir os números
while True:
    # Condicional que se não for atendida quebra o looping
    if termos != quantidade:
        numero = int(input('informe um número para lista: '))
        # Valores só entram na lista de 0 a 1000
        if 0 <= numero <= 1000: 
            lista.append(numero) 
            termos = len(lista)
            print(lista)
        else:
            print('Apenas valores entre 0 e 1000')
    else:
        break


soma = sum(lista)
menor = min(lista)
maior = max(lista)

print(f'Maior valor da lista: {maior}')
print(f'Menor valor da lista: {menor}')
print(f'Soma de todos os valores: {soma}')