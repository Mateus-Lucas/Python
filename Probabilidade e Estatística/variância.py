#Questão 1 - Variância

#Função:
def media_ari(consumo):
  num = 0 
  n = len(consumo) #Contagem do número de elementos
  for i in consumo:
    num = num + i
  media = num/n #calculo da média aritmética
  return media

#Função:
def variancia(consumo):
  med = media_ari(consumo)
  num = 0
  n = len(consumo) #Contagem do número de elementos
  for i in consumo:
     num = num + (i-med)**2 #Calculo variância
  return num/(n-1)

consumo = [10, 13, 17, 9,  8, 11, 13, 7]
import statistics
print('Variância:', variancia(consumo)) 
print('Variância da biblioteca:', statistics.variance(consumo))