#Questão 2 - Moda

#Função:
def moda(escala):
  freq_esc = list() #inicializando lista de frequência
  for i in escala:
    freq_esc.append(escala.count(i)) #Lista de frequência
  freq_max = freq_esc.index(max(freq_esc)) #frequência máxima
  return escala[freq_max] #valor da moda 
  
escala = [67, 75, 63, 72, 77, 78, 81, 77, 80]
import statistics 
print('Moda:', moda(escala))
print('Moda:', statistics.mode(escala))