import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina a largura e a altura da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Corrida")

# Defina a cor de fundo
cor_fundo = (0, 0, 0)

# Defina a posição inicial do carro do jogador
carro_x = largura // 2
carro_y = altura - 100

# Carregue a imagem do carro do jogador
carro_imagem = pygame.image.load("carro.png")  # Certifique-se de ter uma imagem de carro disponível

# Defina a velocidade do carro
velocidade = 5

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        carro_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        carro_x += velocidade

    # Limpe a tela
    tela.fill(cor_fundo)

    # Desenhe o carro do jogador na tela
    tela.blit(carro_imagem, (carro_x, carro_y))

    # Atualize a tela
    pygame.display.flip()
