# Funções a serem exportada

def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco=0):
    dobro = preco * 2
    return dobro


def metade(preco=0):
    metade = preco / 2
    return metade


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')