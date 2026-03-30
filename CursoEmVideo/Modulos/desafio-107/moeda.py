# Funções a serem exportada

def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return f'O valor do aumento é de R${res}'


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return f'O valor da diminuição é de R${res}'


def dobro(preco):
    dobro = preco * 2
    return f'O valor do dobro é R${dobro}'


def metade(preco):
    metade = preco / 2
    return f'O valor da metade R${metade}'