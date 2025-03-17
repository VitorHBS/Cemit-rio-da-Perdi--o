import pygame
from config import PLAYER_GRAVITY, PLAYER_JUMP_STRENGTH, PLAYER_WIDTH, PLAYER_HEIGHT
from entity import Entity

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position, size=(PLAYER_WIDTH, PLAYER_HEIGHT), color=(255, 0, 0))
        self.velocity_y = 0
        self.on_ground = True
        
    def update(self):
        # Aplicar gravidade
        self.velocity_y += PLAYER_GRAVITY
        self.rect.y += self.velocity_y
        
        # Impedir que o jogador caia abaixo do chão
        if self.rect.y >= 400 - self.rect.height - 50:  # Altura da tela - altura do jogador - altura do "chão"
            self.rect.y = 400 - self.rect.height - 50
            self.velocity_y = 0
            self.on_ground = True
    
    def jump(self):
        if self.on_ground:
            self.velocity_y = PLAYER_JUMP_STRENGTH
            self.on_ground = False