import pygame
import random
from config import WIN_WIDTH, WIN_HEIGHT, FPS, ENTITY_SPEED, OBSTACLE_HEIGHT, OBSTACLE_WIDTH
from background import Background
from player import Player
from obstacle import Obstacle

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Corrida Infinita na Floresta")
    clock = pygame.time.Clock()

    # Criar instâncias
    background = Background()
    player = Player("player", (50, WIN_HEIGHT - 90))
    
    obstacles = []
    obstacle_timer = 0
    
    score = 0
    font = pygame.font.SysFont(None, 36)
    
    # Altura do "chão" - ajustar de acordo com a imagem de fundo
    floor_height = 50
    
    running = True
    while running:
        # Gestão de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Gerar obstáculos a cada 1.5 segundos aproximadamente
        obstacle_timer += 1
        if obstacle_timer > FPS * 1.5:
            obstacles.append(Obstacle("obstacle", (WIN_WIDTH, WIN_HEIGHT - floor_height - OBSTACLE_HEIGHT)))
            obstacle_timer = 0
        
        # Atualizar entidades
        background.move()
        player.update()
        
        # Atualizar obstáculos e verificar colisões
        for obstacle in obstacles[:]:
            obstacle.move()
            
            # Remover obstáculos que saíram da tela
            if obstacle.rect.right < 0:
                obstacles.remove(obstacle)
                score += 1
            
            # Verificar colisão
            if player.rect.colliderect(obstacle.rect):
                print("Game Over! Score:", score)
                running = False
        
        # Desenhar elementos
        screen.fill((255, 255, 255))  # Limpar a tela primeiro
        background.draw(screen)
        
        # O chão faz parte da imagem de fundo, então não precisamos desenhar um chão adicional
        # se a sua imagem já incluir o chão
        
        for obstacle in obstacles:
            obstacle.draw(screen)
            
        player.draw(screen)
        
        # Mostrar pontuação
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()