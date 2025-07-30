print('='*11,'| DESAFIO 21 |', '='*11)
'''Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame
import time

# Carrengando e iniciando a música
pygame.init()
pygame.mixer.music.load('desafio-21.mp3')
pygame.mixer.music.play()

# Deixando ela tocar até acabar
while pygame.mixer.music.get_busy():
   time.sleep(1)
