import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configurações da tela
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Função para desenhar a cobra
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Função principal do jogo
def main():
    snake = [[WIDTH // 2, HEIGHT // 2]]
    direction = [0, CELL_SIZE]
    food = [random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE]

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != [0, CELL_SIZE]:
            direction = [0, -CELL_SIZE]
        if keys[pygame.K_DOWN] and direction != [0, -CELL_SIZE]:
            direction = [0, CELL_SIZE]
        if keys[pygame.K_LEFT] and direction != [CELL_SIZE, 0]:
            direction = [-CELL_SIZE, 0]
        if keys[pygame.K_RIGHT] and direction != [-CELL_SIZE, 0]:
            direction = [CELL_SIZE, 0]

        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        snake.insert(0, new_head)

        if snake[0] == food:
            food = [random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                    random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE]
        else:
            snake.pop()

        if (
            snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]
        ):
            running = False

        screen.fill(WHITE)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
        pygame.display.update()

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
