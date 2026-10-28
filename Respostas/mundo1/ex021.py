# Ex021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# [Exemplo] QUANDO O PROGRAMA FOR EXECUTADO A MÚSICA INFORMADA COMEÇARÁ A TOCAR

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while True:
    pygame.event.wait()
