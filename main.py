import pygame
import random
from config import WIN_WIDTH, WIN_HEIGHT, FPS, ENTITY_SPEED, OBSTACLE_HEIGHT, OBSTACLE_WIDTH
from background import Background
from player import Player
from enemy import Enemy

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Corrida Infinita na Floresta")
    clock = pygame.time.Clock()

    background = Background()
    player = Player("player", (50, WIN_HEIGHT - 140))
    
    enemies = []
    enemy_timer = 0
    
    score = 0
    font = pygame.font.SysFont(None, 36)
    
    floor_height = 100
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Gerar inimigos
        enemy_timer += 1
        if enemy_timer > FPS * 1.5:
            enemy_y_position = WIN_HEIGHT - floor_height - OBSTACLE_HEIGHT 
            enemy_x_position = WIN_WIDTH + random.randint(200, 400)
            enemies.append(Enemy("enemy", (enemy_x_position, enemy_y_position)))
            enemy_timer = 0
        
        # Atualizar entidades
        background.move()
        player.update()
        
        for enemy in enemies[:]:
            enemy.move()
            
            if enemy.rect.right < 0:
                enemies.remove(enemy)
                score += 1
            
            # colisão
            if player.rect.colliderect(enemy.rect):
                print("Game Over! Score:", score)
                running = False
        
        # Desenhar elementos
        screen.fill((255, 255, 255))
        background.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)
            
        player.draw(screen)
        
        # Mostrar pontuação
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()