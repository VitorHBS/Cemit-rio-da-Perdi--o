import pygame
import os
from config import ENTITY_SPEED, OBSTACLE_WIDTH, OBSTACLE_HEIGHT
from entity import Entity

class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position, size=(OBSTACLE_WIDTH, OBSTACLE_HEIGHT), color=(0, 0, 255))
        self.image = self.load_image()
        self.rect = self.image.get_rect(topleft=position)
    
    def load_image(self):
        image_path = os.path.join("assets", "enemy", "Rock.png")
        if os.path.exists(image_path):
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
            return image
        else:
            image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
            image.fill((0, 0, 255))
            return image
    
    def move(self):
        self.rect.x -= ENTITY_SPEED["obstacle"]
    
    def draw(self, screen):
        # sombra
        shadow_offset = 5
        shadow_color = (50, 50, 50)
        shadow_rect = self.rect.copy()
        shadow_rect.x += shadow_offset
        shadow_rect.y += shadow_offset
        pygame.draw.ellipse(screen, shadow_color, shadow_rect)
        
        # pedra
        screen.blit(self.image, self.rect)