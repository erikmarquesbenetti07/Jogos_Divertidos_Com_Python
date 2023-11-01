import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Labirinto")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Jogador
player_x, player_y = 50, 50
player_width, player_height = 40, 40
player_speed = 5

# Objetivo
goal_x, goal_y = 700, 500
goal_width, goal_height = 40, 40

# Labirinto
obstacles = [
    pygame.Rect(200, 50, 20, 200),
    pygame.Rect(400, 100, 20, 200),
    pygame.Rect(600, 50, 20, 200),
    pygame.Rect(200, 400, 20, 200),
    pygame.Rect(400, 300, 20, 200),
    pygame.Rect(600, 400, 20, 200)
]

# Função para desenhar o labirinto
def draw_maze():
    for obstacle in obstacles:
        pygame.draw.rect(win, BLACK, obstacle)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimentação do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Colisão com o labirinto
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            player_x, player_y = 50, 50

    # Verifica se o jogador alcançou o objetivo
    if player_rect.colliderect(pygame.Rect(goal_x, goal_y, goal_width, goal_height)):
        print("Você venceu!")
        running = False

    # Limpa a tela
    win.fill(WHITE)

    # Desenha o labirinto
    draw_maze()

    # Desenha o jogador e o objetivo
    pygame.draw.rect(win, BLACK, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(win, BLACK, (goal_x, goal_y, goal_width, goal_height))

    pygame.display.update()

# Encerra o jogo
pygame.quit()
sys.exit()
