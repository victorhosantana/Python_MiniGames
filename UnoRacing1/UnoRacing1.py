#Importação de Módulos e Bibliotecas
import pygame

#Inicialização da biblioteca Pygame
pygame.init()

pygame.display.init()
tela_ativa = True

#Loop princiapl do jogo
while tela_ativa:
    pygame.display.set_mode((800, 600))
    pygame.display.update()




#Finalização do código
pygame.quit()