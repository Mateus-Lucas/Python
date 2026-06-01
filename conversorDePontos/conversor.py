print('=' * 30)
print('CONVERSOR DE PESQUISAS')
print('=' * 30)

print('\n--- VALORES INICIAIS ---')
prime_inicial = int(input('Prime Opinion: '))
toluna_inicial = int(input('Toluna: '))
ysense_inicial = float(input('ySense (US$): '))

print('\n--- VALORES FINAIS ---')
prime_final = int(input('Prime Opinion: '))
toluna_final = int(input('Toluna: '))
ysense_final = float(input('ySense (US$): '))

prime = ((prime_final - prime_inicial) / 100) * 5.04
toluna = (toluna_final - toluna_inicial) / 1360
ysense = (ysense_final - ysense_inicial) * 5.90

total = prime + toluna + ysense
meta = float(input('\nMeta do dia (R$): '))

print(f'''
{'=' * 30}
RESULTADO
{'=' * 30}
Prime Opinion: R$ {prime:.2f}
Toluna:        R$ {toluna:.2f}
ySense:        R$ {ysense:.2f}
------------------------------
Total:         R$ {total:.2f}
''')

if total >= meta:
    print(f'✅ Meta batida! Sobrou R$ {total - meta:.2f}')
else:
    print(f'❌ Faltam R$ {meta - total:.2f}')