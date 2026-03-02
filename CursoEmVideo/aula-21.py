"""
===========================================================
🧠 AULA 21 – FUNÇÕES EM PYTHON
Curso em Vídeo - Professor Guanabara
Resumo organizado por Mateus Lucas
===========================================================
"""

# ===========================================================
# 🔵 1) HELP E DOCUMENTAÇÃO INTERNA
# ===========================================================

# O Python possui documentação interna para funções.

# Exemplo:
# help(print)
# help(input)

# Também podemos acessar usando:
# print(input.__doc__)


# ===========================================================
# 🔵 2) DOCSTRINGS (DOCUMENTAÇÃO PERSONALIZADA)
# ===========================================================

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: não retorna valor (apenas imprime)
    Função criada para fins de estudo.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


# Teste:
# contador(2, 10, 2)
# help(contador)


# ===========================================================
# 🔵 3) PARÂMETROS OPCIONAIS
# ===========================================================

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de até três valores.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: não retorna valor, apenas imprime
    """
    s = a + b + c
    print(f'A soma vale {s}')


# Exemplos de chamada:
# somar(7, 2)
# somar(b=4, a=2)


# ===========================================================
# 🔵 4) ESCOPO DE VARIÁVEIS
# ===========================================================

def teste():
    x = 8  # variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2  # variável global
print(f'No programa principal, n vale {n}')
teste()

# print(x)  # Isso geraria erro (x é local)


# ===========================================================
# 🔵 5) VARIÁVEL GLOBAL (USO DO "global")
# ===========================================================

def funcao():
    global n1  # permite modificar variável global
    n1 = 4
    print(f'n1 dentro da função vale {n1}')


n1 = 2
print(f'n1 antes da função vale {n1}')
funcao()
print(f'n1 depois da função vale {n1}')


# ===========================================================
# 🔵 6) USANDO RETURN
# ===========================================================

def somar_retorno(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar_retorno(3, 2, 5)
r2 = somar_retorno(1, 7)
r3 = somar_retorno(4)

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')


# ===========================================================
# 🔵 7) FUNÇÃO FATORIAL
# ===========================================================

def fatorial(num=1):
    """
    -> Calcula o fatorial de um número.
    :param num: número inteiro
    :return: valor do fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}.')


# ===========================================================
# 🔵 8) FUNÇÃO QUE RETORNA BOOLEANO (PAR OU ÍMPAR)
# ===========================================================

def par(n=0):
    """
    -> Verifica se um número é par.
    :param n: número inteiro
    :return: True se for par, False se não for
    """
    return n % 2 == 0


# Programa principal
num = int(input('Digite um número: '))

if par(num):
    print('É par')
else:
    print('Não é par!')