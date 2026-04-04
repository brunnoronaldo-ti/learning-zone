import pygame
import random

# Inicialização do Pygame
pygame.init()
LARGURA, ALTURA = 600, 400 # Define as dimensões da janela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA)) # Configura a janela do jogo
pygame.display.set_caption("Snake Game") # Define o título da janela do jogo
relogio = pygame.time.Clock() # Controla a taxa de atualização do jogo

