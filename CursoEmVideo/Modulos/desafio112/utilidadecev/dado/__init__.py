def leiaDinheiro(msg):
    valido = False  # Inicia o validador como falso

    while valido == False:  # Loop que executa enquanto o valor não for válido

        # Recebe a entrada do usuário, remove espaços e troca vírgula por ponto
        entrada = str(input(msg)).replace(',', '.').strip()

        # Verifica se a entrada contém apenas letras ou está vazia
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO! Esse preço "{entrada}" não é válido!\033[m')

        else:
            valido = True
            return float(entrada)  # Converte e retorna o valor decimal