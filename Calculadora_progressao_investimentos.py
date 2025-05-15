# investidor_meta.py

def calcular_razao_para_meta(
    saldo_inicial, taxa_juros, tempo_taxa, tempo_investimento, tempo_tipo,
    investimento_inicial, meta
):
    # Convertendo o tempo para meses
    meses = tempo_investimento * 12 if tempo_tipo == 1 else tempo_investimento
    # Convertendo taxa para mensal
    taxa_mensal = (taxa_juros / 100) / 12 if tempo_taxa == 1 else (taxa_juros / 100)

    # Início da simulação para encontrar a razão (acréscimo mensal)
    razao = 0.0
    passo = 0.01  # precisão
    max_tentativas = 100_000
    tentativas = 0

    while tentativas < max_tentativas:
        total = saldo_inicial
        aporte = investimento_inicial
        total_investido = saldo_inicial

        for _ in range(meses):
            total = total * (1 + taxa_mensal) + aporte
            total_investido += aporte
            aporte += razao

        if total >= meta:
            break

        razao += passo
        tentativas += 1

    if tentativas >= max_tentativas:
        return None, None, None
    else:
        return razao, total, total_investido


def main():
    print("=" * 50)
    print("💰 SIMULADOR DE INVESTIMENTO COM PROGRESSÃO ARITMÉTICA")
    print("=" * 50)

    # Entradas do usuário
    saldo_inicial = float(input("Informe o valor inicial disponível (ex: 1412): R$ "))
    taxa_juros = float(input("Informe a taxa de juros (%): "))
    tempo_taxa = int(input("Digite 1 se a taxa é anual ou 2 se for mensal: "))
    tempo_investimento = int(input("Informe o tempo total de investimento (ex: 13): "))
    tempo_tipo = int(input("Digite 1 se o tempo é em anos ou 2 se for em meses: "))
    investimento_inicial = float(input("Informe o valor do investimento mensal inicial (ex: 300): R$ "))
    meta = float(input("Informe o valor da sua meta final (ex: 500000): R$ "))

    razao, total_final, total_investido = calcular_razao_para_meta(
        saldo_inicial, taxa_juros, tempo_taxa,
        tempo_investimento, tempo_tipo,
        investimento_inicial, meta
    )

    print("\n📊 RESULTADO FINAL:")
    if razao is None:
        print("❌ Não foi possível calcular a progressão dentro do limite de tentativas.")
    else:
        meses = tempo_investimento * 12 if tempo_tipo == 1 else tempo_investimento
        total_juros = total_final - total_investido
        print(f"✔ Meta: R$ {meta:,.2f} em {meses} meses")
        print(f"• Aporte inicial: R$ {investimento_inicial:.2f}")
        print(f"• Aumento mensal necessário (razão da PA): R$ {razao:.2f}")
        print(f"• 💵 Total investido (aporte + saldo inicial): R$ {total_investido:,.2f}")
        print(f"• 💸 Total em juros ganhos: R$ {total_juros:,.2f}")
        print(f"• 💰 Valor acumulado ao final: R$ {total_final:,.2f}")

    print("=" * 50)


if __name__ == "__main__":
    main()
