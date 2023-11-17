# 18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
# Considerei todos os meses como 30 dias 

data = str(input('Informe a data no formato dd/mm/aaaa: '))

data_dias_string = data[:2]
data_mes_string = data[2:4]
data_ano_string = data[4:8]

data_dia = int(data_dias_string)
data_mes = int(data_mes_string)
data_ano = int(data_ano_string)

if 0 < data_ano < 2024 and 0 < data_mes <= 12 and 0 < data_dia <= 30:
   if data_mes < 10 and data_dia < 10:
       print(f'A data 0{data_dia}/0{data_mes}/{data_ano} é válida')
   else:
    print(f'A data {data_dia}/{data_mes}/{data_ano} é válida')
else: 
   print('Data inválida')


