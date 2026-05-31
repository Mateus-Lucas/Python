def conversor_prime(pontos):
    return (pontos / 100) * 5.04

def conversor_toluna(pontos):
    return pontos / 1360

def conversor_ysense(valor_dolar):
    return valor_dolar * 5.9


print('=' * 30)
print('CONVERSOR DE PESQUISAS')
print('=' * 30)

prime = conversor_prime(
    int(input('Pontos Prime Opinion: '))
)

toluna = conversor_toluna(
    int(input('Pontos Toluna: '))
)

ysense = conversor_ysense(
    float(input('Valor em dólar no ySense: '))
)

total = prime + toluna + ysense

meta = float(input('Meta do dia (R$): '))

print('\n--- RESULTADO ---')
print(f'Prime Opinion: R$ {prime:.2f}')
print(f'Toluna:        R$ {toluna:.2f}')
print(f'ySense:        R$ {ysense:.2f}')
print(f'Total:         R$ {total:.2f}')

if total >= meta:
    print(f'\n✅ Meta batida! Você ultrapassou em R$ {total - meta:.2f}')
else:
    print(f'\n❌ Ainda faltam R$ {meta - total:.2f} para atingir a meta.')