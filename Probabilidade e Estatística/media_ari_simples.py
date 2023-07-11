#Questão 1 - Média aritmética simples

#Função:
def media_ari(consumo):
  num = 0 
  n = len(consumo) #Contagem do número de elementos
  for i in consumo:
    num = num + i
  media = num/n #calculo da média aritmética
  return media

consumo = [10, 13, 17, 9,  8, 11, 13, 7]
import statistics 
print('Média aritimética:', media_ari(consumo))
print('Média aritimética da biblioteca:', statistics.mean(consumo))