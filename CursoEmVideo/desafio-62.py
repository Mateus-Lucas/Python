from time import sleep

def linha():
    print('\033[1;33m=\033[m' * 40)

linha()
print(' ' * 10, '\033[1;33m10 TERMOS DE UMA PA\033[m')
linha()

# p1 = primeiro termo | r = razão | c = contador (posição do termo) 
p1 = int(input('\033[1;36mInforme o primeiro termo:\033[m '))
r = int(input('\033[1;36mInforme a razão dessa PA:\033[m '))
c = 1

print('\n\033[1;34mCalculando a progressão...\033[m\n')
sleep(1)

linha()
# imprime os 10 primeiros termos
while c <= 10:
    t = p1 + (c - 1) * r
    print(f'\033[1;33m{c}º termo\033[m = \033[1;32m{t}\033[m')
    sleep(0.2)
    c += 1
linha()

# t_a = Termos adicionais 
# agora c já vale 11 (próximo termo a ser mostrado)
while True:
    t_a = int(input('Você quer adicionar mais algum termo? Quantos? (0 para sair) '))
    if t_a <= 0:   # 0 ou negativo encerra
        break

    # imprime exatamente t_a termos, continuando a partir de c
    for _ in range(t_a):
        t = p1 + (c - 1) * r
        sleep(0.2)
        print(f'\033[1;33m{c}º termo\033[m = \033[1;32m{t}\033[m')
        c += 1  # importante: avançar o contador para o próximo termo

    linha()

print('\n\033[1;32mFIM DA PROGRESSÃO ARITMÉTICA!\033[m')
