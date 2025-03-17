from config import ENTITY_SPEED, OBSTACLE_WIDTH, OBSTACLE_HEIGHT
from entity import Entity

class Obstacle(Entity):
    def __init__(self, name, position):
        super().__init__(name, position, size=(OBSTACLE_WIDTH, OBSTACLE_HEIGHT), color=(0, 0, 255))
    
    def move(self):
        self.rect.x -= ENTITY_SPEED[self.name]