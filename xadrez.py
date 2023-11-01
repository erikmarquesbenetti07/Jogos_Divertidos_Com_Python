import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Defina o tamanho da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Tamanho do tabuleiro e tamanho de cada quadrado
BOARD_SIZE = 8
SQUARE_SIZE = SCREEN_WIDTH // BOARD_SIZE

# Inicialize a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Xadrez")

# Função para desenhar o tabuleiro
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Função para desenhar as peças
def draw_pieces():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 0:
                # Peças brancas (círculos brancos)
                pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)
            else:
                # Peças pretas (círculos pretos)
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpe a tela
    screen.fill(WHITE)

    # Desenhe o tabuleiro
    draw_board()

    # Desenhe as peças
    draw_pieces()

    pygame.display.flip()

# Encerre o Pygame
pygame.quit()
sys.exit()
