import pygame
import random
import time

# Inicialização do Pygame
pygame.init()

# Dimensões da janela
WIDTH, HEIGHT = 400, 400
TILE_SIZE = WIDTH // 4

# Cores
BLACK = (0, 0, 0)

# Tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quebra-Cabeça Deslizante")

# Números para a grade
numbers = list(range(1, 16))
numbers.append(0)

# Posição da peça vazia
empty_position = (3, 3)

# Tempos para mostrar a grade inicial e a duração do jogo
SHOW_INITIAL_GRID_TIME = 3
GAME_TIME = 60

# Função para embaralhar os números
def shuffle_numbers():
    random.shuffle(numbers)

# Função para desenhar a grade na tela
def draw_grid():
    for i in range(16):
        number = numbers[i]
        x, y = i % 4, i // 4
        if number > 0:
            pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            font = pygame.font.Font(None, 36)
            text = font.render(str(number), True, (255, 255, 255))
            screen.blit(text, (x * TILE_SIZE + TILE_SIZE // 2 - 10, y * TILE_SIZE + TILE_SIZE // 2 - 20))

# Inicialmente, mostre a grade por alguns segundos
shuffle_numbers()
show_initial_grid_start = time.time()
while time.time() - show_initial_grid_start < SHOW_INITIAL_GRID_TIME:
    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()

# Loop principal
game_start = time.time()
while time.time() - game_start < GAME_TIME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= TILE_SIZE
            y //= TILE_SIZE
            if (x, y) == empty_position:
                continue
            if (abs(x - empty_position[0]) + abs(y - empty_position[1])) == 1:
                i = x + y * 4
                empty_i = empty_position[0] + empty_position[1] * 4
                numbers[i], numbers[empty_i] = numbers[empty_i], numbers[i]
                empty_position = (x, y)

    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()

pygame.quit()
