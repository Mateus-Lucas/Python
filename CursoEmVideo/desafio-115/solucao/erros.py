import cores


def tratamento_erro(msg):
    while True:
        try:
            num = int(input(msg))

            if 1 <= num <= 3:
                return num

            print(cores.cor_vermelho(
                'ERRO! Digite uma opção entre 1 e 3.'
            ))

        except (ValueError, TypeError):
            print(
                cores.cor_vermelho(
                    'ERRO: por favor, digite um número inteiro válido.'
                )
            )

        except KeyboardInterrupt:
            print(
                cores.cor_vermelho(
                    '\nUsuário não quis informar um número.'
                )
            )
            return 3