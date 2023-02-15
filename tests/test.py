import time
import os
import pygame

songs = ['rocket.mp3', 'song2.mp3', 'song3.mp3']

untalked = input(">>> ")
talk = (untalked.lower())

if 'play' in talk:
    
    for song in songs:
        if song[:-4].lower() in talk:
            pygame.init()
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            print("Playing "+ song[:-4])
            break
    else:
        print("We Don't Have That Song!")
    
    untalked = input(">>> ")
    talk = (untalked.lower())