print('\033[1;33m' + '=' * 20 + ' | Desafio 102 | ' + '=' * 20 + '\033[m')

''' Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial'''

# CÓDIGO GUAMABARA
def fatorial(n, show=False):
    """
        --> Calcula o fatorial de um número.

        :param num: Número a ser calculado
        :param show: (Opcional) Mostra o cálculo se True
        :return: Valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# CÓDIGO PESSOAL
# def fatorial(num, show=False):
#     """
#     --> Calcula o fatorial de um número.

#     :param num: Número a ser calculado
#     :param show: (Opcional) Mostra o cálculo se True
#     :return: Valor do fatorial
#     """
#     f = 1

#     if show:
#         for i in range(num, 0, -1):
#             print(i, end=' x ' if i > 1 else ' = ')

#     for i in range(num, 0, -1):
#         f *= i

#     return f


# Programa principal
print(fatorial(7, show=True))
help(fatorial)