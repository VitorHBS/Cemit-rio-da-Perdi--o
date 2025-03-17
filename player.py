import pygame
import os
from config import PLAYER_GRAVITY, PLAYER_JUMP_STRENGTH, WIN_HEIGHT
from entity import Entity

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position, size=(50, 50), color=(255, 0, 0))
        self.velocity_y = 0
        self.on_ground = True
        self.jump_count = 0  # Contador de saltos
        self.image = self.load_image()
        self.rect = self.image.get_rect(topleft=position)
        
    def load_image(self):
        image_path = os.path.join(r"c:\Users\Vitor\Desktop\Cemitério-da-Perdição\assets\Player", "Player.png")
        if os.path.exists(image_path):
            image = pygame.image.load(image_path).convert_alpha()
            return image
        else:
            image = pygame.Surface((50, 50))
            image.fill((255, 0, 0))
            return image
    
    def update(self):
        # Aplicar gravidade
        self.velocity_y += PLAYER_GRAVITY
        self.rect.y += self.velocity_y
        
        # Impedir que o jogador caia abaixo do chão
        floor_height = 100  # Ajuste a altura do chão aqui
        if self.rect.y >= WIN_HEIGHT - self.rect.height - floor_height:
            self.rect.y = WIN_HEIGHT - self.rect.height - floor_height
            self.velocity_y = 0
            self.on_ground = True
            self.jump_count = 0  # Resetar o contador de saltos quando o jogador tocar o chão
    
    def jump(self):
        if self.on_ground or self.jump_count < 2:  # Permitir um segundo salto
            self.velocity_y = PLAYER_JUMP_STRENGTH
            self.on_ground = False
            self.jump_count += 1  # Incrementar o contador de saltos