import pygame
import os

class Entity:
    def __init__(self, name: str, position: tuple, size=(800, 400), color=(200, 200, 200)):
        self.name = name
        
        # Para o background, carregar da pasta assets
        if name == "background":
            self.image = pygame.Surface(size)
        
        # Para player, a imagem será definida posteriormente
        elif name == "player":
            self.image = None
            
        # Para obstáculo, criar um retângulo marrom
        elif name == "obstacle":
            self.image = pygame.Surface((30, 50))
            self.image.fill((139, 69, 19))  # Cor marrom para obstáculos tipo árvore
        
        # Para inimigos, a imagem será definida posteriormente
        else:
            self.image = None
            
        self.rect = self.image.get_rect(topleft=position) if self.image else pygame.Rect(position, (50, 50))

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)