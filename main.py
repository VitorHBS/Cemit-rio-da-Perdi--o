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

    # Criar instâncias
    background = Background()
    player = Player("player", (50, WIN_HEIGHT - 140))  # Ajuste a posição Y inicial do jogador aqui
    
    enemies = []
    enemy_timer = 0
    
    score = 0
    font = pygame.font.SysFont(None, 36)
    
    # Altura do "chão" - ajustar de acordo com a imagem de fundo
    floor_height = 100  # Ajuste a altura do chão aqui
    
    running = True
    while running:
        # Gestão de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Gerar inimigos a cada 1.5 segundos aproximadamente
        enemy_timer += 1
        if enemy_timer > FPS * 1.5:
            # Ajuste a posição Y aqui para mover as pedras mais para cima ou mais para baixo
            enemy_y_position = WIN_HEIGHT - floor_height - OBSTACLE_HEIGHT  # Ajuste conforme necessário
            # Ajuste a posição X aqui para garantir espaçamento adequado entre as pedras
            enemy_x_position = WIN_WIDTH + random.randint(200, 400)  # Aumente o intervalo conforme necessário
            enemies.append(Enemy("enemy", (enemy_x_position, enemy_y_position)))
            enemy_timer = 0
        
        # Atualizar entidades
        background.move()
        player.update()
        
        # Atualizar inimigos e verificar colisões
        for enemy in enemies[:]:
            enemy.move()
            
            # Remover inimigos que saíram da tela
            if enemy.rect.right < 0:
                enemies.remove(enemy)
                score += 1
            
            # Verificar colisão
            if player.rect.colliderect(enemy.rect):
                print("Game Over! Score:", score)
                running = False
        
        # Desenhar elementos
        screen.fill((255, 255, 255))  # Limpar a tela primeiro
        background.draw(screen)
        
        # O chão faz parte da imagem de fundo, então não precisamos desenhar um chão adicional
        # se a sua imagem já incluir o chão
        
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