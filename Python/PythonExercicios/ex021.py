print('====== EX 021 ======')
# Faça um programa em python que abra e reproduza o audio de um arquivo MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('buttercup.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
