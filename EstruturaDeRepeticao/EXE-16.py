# 16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

a = 1
b = 1

print(a, end=' ') # imprime o primeiro número da série
while a < 500:
    a, b = b, a + b  # atualiza os valores de a e b corretamente
    print(a, end=' ') # imprime o próximo número da série


