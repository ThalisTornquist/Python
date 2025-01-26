import pygame

pygame.mixer.init() #inicia o player de musica

pygame.mixer.music.load("C:/Users/thali/Downloads/musica.mp3") #o link da musica

pygame.mixer.music.play() #da play na musica

# "C:\Users\thali\Downloads\musica.mp3"

input('Pressione Enter para parar.')
#comando para parar com a função de baixo
pygame.mixer.music.stop()

