# Funções a serem exportada

def aumentar(preco=0, taxa=0, formatado=False):
    res = preco + (preco * taxa/100)
    return res if not formatado else moeda(res)


def diminuir(preco=0, taxa=0, formatado=False):
    res = preco - (preco * taxa/100)
    return res if not formatado else moeda(res)


def dobro(preco=0, formatado=False):
    dobro = preco * 2
    return dobro if not formatado else moeda(dobro)


def metade(preco=0, formatado=False):
    metade = preco / 2
    return metade if not formatado else moeda(metade)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxa_aum=10, taxa_red=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(preco, taxa_aum, True)}')
    print(f'{taxa_red}% de redução: \t{diminuir(preco, taxa_red, True)}')