import pygame
pygame.init()

class Player (pygame.sprite.Sprite):

    def __init__ (self, posição):
        super().__init__()
        self.x,self.y = posição[0], posição[1] 
        self.image = pygame.image.load("../Sprites/Bonus/PNG/Transperent/Icon49.png")
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.velocidade_y = 0
        self.gravidade = 1000
        self.estado = 'parado'

    def draw (self):
        self.tela = pygame.display.get_surface()
        self.tela.blit(self.image, (self.x,self.y))

    def pula(self):
        if self.estado == 'parado':
            self.velocidade_y -= 300
            self.estado = 'pulando'