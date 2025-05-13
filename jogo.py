import pygame
from player import *

pygame.init()

# ----- Gera tela principal
info = pygame.display.Info()
width, height = info.current_w, info.current_h
tela = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

pygame.display.set_caption('Muse Dash')

# ----- Inicia estruturas de dados
game = True

y = tela.get_height() - 300
x = 10


# ===== Loop principal =====
while game:

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jogador.pula()
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    tela.fill((255, 255, 255))  # Preenche com a cor branca

    # ---------------- chão
    cor = (0, 0, 0)
    vertices = (0, tela.get_height() - 200, tela.get_width(), 200) 
    pygame.Surface
    pygame.draw.rect(tela, cor, vertices)
    rect_chão = pygame.Rect(0, tela.get_height() - 200, tela.get_width(), 200) 

    # ----------------

    jogador = Player((x,y))
    print("cheguei aqui")
    jogador.draw()
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados