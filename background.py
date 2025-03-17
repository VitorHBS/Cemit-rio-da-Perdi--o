from config import ENTITY_SPEED
import os
import pygame

class Background:
    def __init__(self):
        self.layers = self.load_layers()
        
    def load_layers(self):
        # Carregar todas as imagens de background da pasta assets
        image_files = [
            "sky.png",
            "back_trees.png",
            "tree.png",
            "crypt.png",
            "graves.png",
            "bones.png",
            "wall.png",
            "ground.png"
        ]
        layers = []
        for i, image_file in enumerate(image_files):
            image_path = os.path.join("c:\\Users\\Vitor\\Desktop\\Trabalho facu\\endless_runner\\assets", image_file)
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (800, 400))
            layer = {
                "image": image,
                "rect1": image.get_rect(topleft=(0, 0)),
                "rect2": image.get_rect(topleft=(800, 0)),
                "speed": ENTITY_SPEED["background"] * (i + 1) / len(image_files)  # Velocidade diferente para cada camada
            }
            layers.append(layer)
        return layers

    def move(self):
        for layer in self.layers:
            layer["rect1"].x -= layer["speed"]
            layer["rect2"].x -= layer["speed"]

            # Reposicionamento do fundo para efeito de rolagem infinita
            if layer["rect1"].right <= 0:
                layer["rect1"].left = layer["rect2"].right
            if layer["rect2"].right <= 0:
                layer["rect2"].left = layer["rect1"].right

    def draw(self, screen):
        for layer in self.layers:
            screen.blit(layer["image"], layer["rect1"])
            screen.blit(layer["image"], layer["rect2"])