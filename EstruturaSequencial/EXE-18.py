# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input('Informe o tamanho do arquivo em MB: '))
velociade_link = float(input('Informe a velocidade do link em MBPS: '))

#calculo para calcular o tempo do download
tempo_download = tamanho_arquivo/velociade_link

print(f'O tempo para baixar esse arquivo é aproximadamente {tempo_download/60:.1f} minutos')


