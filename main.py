# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

ANCHO_VENTANA = 600
ALTO_VENTANA = 400

ANCHO_PALETA = 10
ALTO_PALETA = 60

LADO_PELOTA = 10

VELOCIDADE_PALETA = 10

PALETA_ESQUERDA_X = 0
PALETA_DEREITA_X = ANCHO_VENTANA - ANCHO_PALETA

paleta_esquerda_y = paleta_dereita_y = ALTO_VENTANA/2 - ALTO_PALETA/2

pelota_x = ANCHO_VENTANA/2 - LADO_PELOTA/2
pelota_y = ALTO_VENTANA/2 - LADO_PELOTA/2

pygame.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA),0,32)
pygame.display.set_caption("Python_Pong")

ON = True

while ON:
    
    reloj = pygame.time.Clock()
    
    ventana.fill((0,0,0))
    
    imagen_paleta_esquerda = pygame.Rect(PALETA_ESQUERDA_X, paleta_esquerda_y, ANCHO_PALETA, ALTO_PALETA)
    pygame.draw.rect(ventana, (255,255,255), imagen_paleta_esquerda)
    
    pygame.display.update()
    
    tecla_presionada = pygame.key.get_pressed()
    if tecla_presionada[K_DOWN] and paleta_esquerda_y < ALTO_VENTANA-ALTO_PALETA:
        paleta_esquerda_y = paleta_esquerda_y + VELOCIDADE_PALETA
    if tecla_presionada[K_UP] and paleta_esquerda_y > 0:
        paleta_esquerda_y = paleta_esquerda_y - VELOCIDADE_PALETA
        
    if paleta_esquerda_y < 0:
        paleta_esquerda_y = 0
    if paleta_esquerda_y > ALTO_VENTANA-ALTO_PALETA:
        paleta_esquerda_y = ALTO_VENTANA-ALTO_PALETA
    
    
    
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.display.quit()
            ON = False

    reloj.tick(60)