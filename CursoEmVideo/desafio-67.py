print('\033[1;33m' + '=' * 20, '| Desafio 67 |' , '=' * 20 + '\033[m')

'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado 
pelo usuário. O programa será interrompido quando o número solicitado for negativo
'''

from time import sleep 

def linha():  # função para separar visualmente as seções
    print('-' * 40)

linha()
print('Bem vindo ao looping da tabuada')
linha()

while True:
    n = int(input('Informe um número para a tabuada: '))
    if n < 0:  # condição de parada
        print('\033[1;31mEncerrando... Número negativo informado!\033[m')
        break
    
    for i in range(1, 11):  # tabuada de 1 a 10
        print(f'{n} x {i} = {n * i}')
        sleep(0.3)  # pausa para melhor visualização
    
    linha()

linha()
print('\033[1;32mTabuada encerrada com sucesso!\033[m')

print('Tabuada acabou')
    