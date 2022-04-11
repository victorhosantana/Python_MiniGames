#Importação de Módulos e Bibliotecas
import pygame

#Inicialização do módulo Pygame
pygame.init()
pygame.display.init()

#Definição de quantidade de movimento dos objetos, em px
movimento = 20

#Definição da posição inicial dos objetos
pos_uno_x = 400
pos_uno_y = 300


#Definindo a tela, o nome e o tamanho do display
tela = pygame.display.set_mode((800, 600)) #Define a variável tela e o tamanho em px
pygame.display.set_caption('UnoRacing') #Muda o título da tela
tela_ativa = True #Torna a tela visível para o loop principal funcionar

#Loop principal do jogo
while tela_ativa:

    #Tempo de atualização da tela
    pygame.time.delay(30)
    
    #Loop de recebimento dos comandos
    for evento in pygame.event.get():
        
        #Evento de fechar o jogo
        if evento.type == pygame.QUIT:
            tela_ativa = False
    
    #Obtendo os comandos do objeto Uno, a partir da tecla apertada
    comandos = pygame.key.get_pressed()

    #Sequência de comandos do objeto Uno
    if comandos[pygame.K_UP]: #Movimento para cima
        pos_uno_y -= movimento
    if comandos[pygame.K_DOWN]: #Movimento para baixo
        pos_uno_y += movimento
    if comandos[pygame.K_RIGHT]: #Movimento para direita
        pos_uno_x += movimento
    if comandos[pygame.K_LEFT]: #Movimento para esquerda
        pos_uno_x -= movimento
    
    #Limpa a tela para o próximo movimento
    tela.fill((0, 0, 0)) #Define como fundo preto

    #Desenha um objeto na tela
    pygame.draw.circle(tela, (100, 0, 255), (pos_uno_x, pos_uno_y), 30)

    #Atualiza a tela com os comandos e movimentos
    pygame.display.update()


#Finalização do módulo Pygame
pygame.quit()