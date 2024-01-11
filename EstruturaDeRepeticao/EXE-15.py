# 15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

def serie_fibonacci(n):
    a, b = 1, 1
    print(a, end=' ')  # imprime o primeiro número da série
    for _ in range(n - 1):
        a, b = b, a + b  # atualiza os valores de a e b corretamente
        print(a, end=' ')  # imprime o próximo número da série

numero = 9  # o usuário deseja gerar a série até o 9-ésimo termo
serie_fibonacci(numero)


