import pygame
import sys
import time

pygame.init()

#config do jogo
#--------------------------------------------------
velocidade_jogo = 60
tempodojogo = pygame.time.Clock()
largura, altura = 1250, 720
tela = pygame.display.set_mode((largura, altura))
chaoinicio = [0, altura]
chaofim = [largura, altura]
colisao_chao = [chaoinicio, chaofim]
vermelho = (200, 0, 0)
preto = (0, 0, 0)
verde = (0, 150, 0)
azul = (0, 0, 150)
#-------------------------------------------------

#config do quadrado
#-------------------------------------------------
quadrado = [50, 620 ,20, 50]
quadrado_vel = 0
gravidade = 1
#-------------------------------------------------

#config circulo
#-------------------------------------------------
circulo = [1200, 650]
circulo_vel = 5
raio = 10
#-------------------------------------------------

no_ar = False

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not no_ar:
                quadrado_vel = -20
                no_ar = True
    
    
    circulo[0] -= circulo_vel
    if circulo[0] + raio < 0:
        circulo[0] = largura + raio
        
    
    quadrado[1] += quadrado_vel
    quadrado_vel += gravidade
    
    if quadrado[1] >= 620:
        quadrado[1] = 620
        quadrado_vel = 0
        no_ar = False
    
        
    tela.fill(azul)        
    
    pygame.draw.circle(tela, vermelho, circulo, raio)
    pygame.draw.rect(tela, preto, quadrado)
    pygame.draw.line(tela, verde, chaoinicio, chaofim, 100)
    tempodojogo.tick(velocidade_jogo)
    pygame.display.flip()

