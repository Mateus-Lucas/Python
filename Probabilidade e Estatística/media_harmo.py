#Questão 2 - Média_harmônica 

def media_harm(escala):
  num = 0 
  n = len(escala) #Contagem do número de elementos
  for i in escala:
    num = num + 1/i
  media_h = n/num #calculo da média harmônica
  return media_h

escala = [67, 75, 63, 72, 77, 78, 81, 77, 80]
import statistics

print('Média harmônica:',media_harm(escala))
print('Média harmônica biblioteca:', statistics.harmonic_mean(escala))

