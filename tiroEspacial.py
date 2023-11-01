import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definir as dimensões da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Posição inicial da nave
nave_x = largura // 2
nave_y = altura - 50
nave_largura = 40
nave_altura = 20

# Posições iniciais dos inimigos
inimigos = []
inimigo_largura = 20
inimigo_altura = 20

for _ in range(5):
    inimigo_x = random.randint(0, largura - inimigo_largura)
    inimigo_y = random.randint(0, altura // 2)
    inimigos.append([inimigo_x, inimigo_y])

# Velocidade da nave
velocidade_nave = 5

# Velocidade dos inimigos
velocidade_inimigos = 3

# Loop do Jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controles da nave
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        nave_x -= velocidade_nave
    if keys[pygame.K_RIGHT]:
        nave_x += velocidade_nave

    # Atualizar posição dos inimigos
    for i, inimigo in enumerate(inimigos):
        inimigo[1] += velocidade_inimigos
        if inimigo[1] > altura:
            inimigos[i] = [random.randint(0, largura - inimigo_largura), random.randint(0, altura // 2)]

    # Verificar colisões
    for inimigo in inimigos:
        if nave_x < inimigo[0] + inimigo_largura and nave_x + nave_largura > inimigo[0] and \
           nave_y < inimigo[1] + inimigo_altura and nave_y + nave_altura > inimigo[1]:
            running = False

    # Limpar a tela
    tela.fill(branco)

    # Desenhar a nave
    pygame.draw.rect(tela, vermelho, (nave_x, nave_y, nave_largura, nave_altura))

    # Desenhar os inimigos
    for inimigo in inimigos:
        pygame.draw.circle(tela, vermelho, (inimigo[0] + inimigo_largura // 2, inimigo[1] + inimigo_altura // 2), inimigo_largura // 2)

    pygame.display.update()

# Finalizar o jogo
pygame.quit()
