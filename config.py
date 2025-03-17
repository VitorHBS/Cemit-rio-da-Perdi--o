# config.py

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Configurações do jogador
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_COLOR = RED
PLAYER_GRAVITY = 0.6
PLAYER_JUMP_STRENGTH = -10

# Configurações do obstáculo
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 50
OBSTACLE_COLOR = BLUE
OBSTACLE_SPEED = 6

# Configurações do jogo
FPS = 30


# Configurações velocidade
WIN_WIDTH = 800
WIN_HEIGHT = 400
ENTITY_SPEED = {
    "background": 3,  # Velocidade do fundo
    "player": 0,
    "obstacle": 6,
}