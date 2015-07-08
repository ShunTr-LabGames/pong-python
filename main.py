# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

ANCHO_VENTANA = 600
ALTO_VENTANA = 400

ANCHO_PALETA = 10
ALTO_PALETA = 60

LADO_PELOTA = 10

LADO_CADRADO_MEDIO = 5

VELOCIDADE_PALETA = 10

VELOCIDADE_PELOTA_X = 5
VELOCIDADE_PELOTA_Y = 5

PALETA_ESQUERDA_X = 0
PALETA_DEREITA_X = ANCHO_VENTANA - ANCHO_PALETA

paleta_esquerda_y = paleta_dereita_y = ALTO_VENTANA/2 - ALTO_PALETA/2

pelota_x = ANCHO_VENTANA/2 - LADO_PELOTA/2
pelota_y = ALTO_VENTANA/2 - LADO_PELOTA/2

pygame.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA),0,32)
pygame.display.set_caption("Python_Pong")

pausa = 30

ON = True

while ON:
    
    reloj = pygame.time.Clock()
    
    ventana.fill((0,0,0))
    
    #IMAXES:
    
    for contador in range(0,ALTO_VENTANA,LADO_CADRADO_MEDIO*2):
        cadrado_medio = pygame.Rect((ANCHO_VENTANA/2 - LADO_CADRADO_MEDIO/2),contador,LADO_CADRADO_MEDIO,LADO_CADRADO_MEDIO)
        pygame.draw.rect(ventana, (255,255,255), cadrado_medio)
    
    imagen_paleta_esquerda = pygame.Rect(PALETA_ESQUERDA_X, paleta_esquerda_y, ANCHO_PALETA, ALTO_PALETA)
    pygame.draw.rect(ventana, (255,255,255), imagen_paleta_esquerda)
    
    imagen_paleta_dereita = pygame.Rect(PALETA_DEREITA_X,paleta_dereita_y,ANCHO_PALETA, ALTO_PALETA)
    pygame.draw.rect(ventana,(255,255,255), imagen_paleta_dereita)
    
    imagen_pelota = pygame.Rect(pelota_x, pelota_y, LADO_PELOTA, LADO_PELOTA)
    pygame.draw.rect(ventana, (255,255,255), imagen_pelota)
    
    #pygame.draw.line(ventana, (255,0,0), (ANCHO_VENTANA/2,0),(ANCHO_VENTANA/2,ALTO_VENTANA))
    #pygame.draw.line(ventana, (255,0,0), (0,ALTO_VENTANA/2),(ANCHO_VENTANA,ALTO_VENTANA/2))
    
    pygame.display.update()
    
    #MOVEMENTOS:
    
    tecla_presionada = pygame.key.get_pressed()
    if tecla_presionada[K_DOWN] and paleta_esquerda_y < ALTO_VENTANA-ALTO_PALETA:
        paleta_esquerda_y = paleta_esquerda_y + VELOCIDADE_PALETA
    if tecla_presionada[K_UP] and paleta_esquerda_y > 0:
        paleta_esquerda_y = paleta_esquerda_y - VELOCIDADE_PALETA
        
    if paleta_esquerda_y < 0:
        paleta_esquerda_y = 0
    if paleta_esquerda_y > ALTO_VENTANA-ALTO_PALETA:
        paleta_esquerda_y = ALTO_VENTANA-ALTO_PALETA
        
    paleta_dereita_y = pelota_y-(ALTO_PALETA/2)
    
    if pelota_y >= paleta_dereita_y and pelota_y <= paleta_dereita_y+ALTO_PALETA and pelota_x >= PALETA_DEREITA_X-LADO_PELOTA and pelota_x < PALETA_DEREITA_X:
        #VELOCIDADE_PELOTA_Y = -VELOCIDADE_PELOTA_Y
        VELOCIDADE_PELOTA_X = -VELOCIDADE_PELOTA_X
        
    if pelota_y >= paleta_esquerda_y and pelota_y <= paleta_esquerda_y+ALTO_PALETA and pelota_x > PALETA_ESQUERDA_X and pelota_x < PALETA_ESQUERDA_X + ANCHO_PALETA:
        #VELOCIDADE_PELOTA_Y = -VELOCIDADE_PELOTA_Y
        VELOCIDADE_PELOTA_X = -VELOCIDADE_PELOTA_X
    
    #MOVEMENTO PELOTA:
    
    if pausa == 0:
        pelota_x = pelota_x + VELOCIDADE_PELOTA_X
        pelota_y += VELOCIDADE_PELOTA_Y
    
    if pausa > 0:
        pausa -= 1
    
    if pelota_y >= ALTO_VENTANA-LADO_PELOTA:
        VELOCIDADE_PELOTA_Y = -VELOCIDADE_PELOTA_Y
    if pelota_y <= 0:
        VELOCIDADE_PELOTA_Y = -VELOCIDADE_PELOTA_Y
        
    if pelota_x < -LADO_PELOTA:
        pelota_x = ANCHO_VENTANA/2 - LADO_PELOTA/2
        pelota_y = ALTO_VENTANA/2 - LADO_PELOTA/2
        VELOCIDADE_PELOTA_X = -VELOCIDADE_PELOTA_X
        pausa = 30
        
    if pelota_x > ANCHO_VENTANA:
        pelota_x = ANCHO_VENTANA/2 - LADO_PELOTA/2
        pelota_y = ALTO_VENTANA/2 - LADO_PELOTA/2
        VELOCIDADE_PELOTA_X = -VELOCIDADE_PELOTA_X
        pausa = 30
    
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.display.quit()
            ON = False

    reloj.tick(60)