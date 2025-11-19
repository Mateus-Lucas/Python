n = s = 0  # Aqui estamos criando duas variáveis de uma vez:
           # n será o número digitado
           # s será a soma total

while True:  # Loop infinito (vai repetir para sempre)
    n = int(input('Digite um número: '))  # Usuário informa um número
    
    if n == 999:   # Condição de parada (sentinela)
        break      # Interrompe o while
    
    s += n  # Acumula o valor dentro de s

print(f'A soma vale {s}')  # Mostramos o resultado depois do loop
