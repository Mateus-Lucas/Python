#Questão 2 - Mediana 

#Função:
def mediana(escala):
  escala.sort() #ordenando a escala
  n = len(escala) #contagem dos elemento
  if n%2==0: # n é par
    pos1 = n/2 - 1 
    pos2 = n/2
    media = (escala[pos1] + escala[pos2])/2
  else: # n é impar
    pos = (n-1)/2
    media = escala[int(pos)]
  return media

import statistics
escala = [67, 75, 63, 72, 77, 78, 81, 77, 80]
print('Mediana:', mediana(escala))
print('Mediana biblioteca:', statistics.median(escala))