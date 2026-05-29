def printErro(msg):
    print(f'\033[1;31m{msg}\033[m')

try:
    # O usuário digita dois números
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    # Tentativa de divisão
    r = a / b

# Erro caso o usuário digite letras ou valores inválidos
except (ValueError, TypeError):
    printErro('Tivemos um problema com os tipos de dados digitados.')

# Erro caso o denominador seja 0
except ZeroDivisionError:
    printErro('Não é possível dividir um número por zero!')

# Erro caso o usuário interrompa o programa (CTRL + C)
except KeyboardInterrupt:
    printErro('O usuário preferiu não informar os dados.')

# Captura qualquer outro erro não tratado acima
except Exception as erro:
    printErro(f'O problema encontrado foi: {erro.__class__.__name__}')

# Executa se NÃO acontecer nenhum erro
else:
    printErro(f'O resultado da divisão é {r}')

# Sempre será executado, com erro ou sem erro
finally:
    print('Volte sempre! Muito obrigado!')