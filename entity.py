import pygame
import os

class Entity:
    def __init__(self, name: str, position: tuple, size=(800, 400), color=(200, 200, 200)):
        self.name = name
        
        # Para o background, carregar da pasta assets
        if name == "background":
            self.image = pygame.Surface(size)
        
        # Para player, criar um retângulo vermelho
        elif name == "player":
            self.image = pygame.Surface((40, 40))
            self.image.fill((255, 0, 0))
            
        # Para obstáculo, criar um retângulo marrom
        elif name == "obstacle":
            self.image = pygame.Surface((30, 50))
            self.image.fill((139, 69, 19))  # Cor marrom para obstáculos tipo árvore
            
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)