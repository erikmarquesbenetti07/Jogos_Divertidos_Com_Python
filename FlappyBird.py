import pygame
import sys
import time

# Inicialização do Pygame
pygame.init()

# Configurações
largura_tela = 400
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Flappy Bird Clone")

# Cores
branco = (255, 255, 255)
azul = (0, 0, 255)

# Posição inicial do pássaro
x_passaro = 100
y_passaro = altura_tela // 2
velocidade_passaro = 0

# Posição inicial dos obstáculos
x_obstaculo = largura_tela
altura_obstaculo = 200
espaco_entre_obstaculos = 150
largura_obstaculo = 50
velocidade_obstaculos = 2

# Função para desenhar o pássaro
def desenhar_passaro(x, y):
    pygame.draw.rect(tela, azul, (x, y, 30, 30))

# Função para desenhar os obstáculos
def desenhar_obstaculo(x, altura):
    pygame.draw.rect(tela, azul, (x, 0, largura_obstaculo, altura))
    pygame.draw.rect(tela, azul, (x, altura + espaco_entre_obstaculos, largura_obstaculo, altura_tela - altura - espaco_entre_obstaculos))

# Variável para controlar o estado do jogo
jogo_ativo = True

# Loop principal do jogo
while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if y_passaro > 0:  # Impedir que o pássaro voe para cima fora da tela
                    velocidade_passaro = -5

    # Atualização da posição do pássaro
    y_passaro += velocidade_passaro
    velocidade_passaro += 0.2

    # Movimento dos obstáculos
    x_obstaculo -= velocidade_obstaculos

    # Verificação de colisão com os obstáculos
    if x_obstaculo < -largura_obstaculo:
        x_obstaculo = largura_tela
        altura_obstaculo = 200

    if x_passaro + 30 > x_obstaculo and x_passaro < x_obstaculo + largura_obstaculo:
        if y_passaro < altura_obstaculo or y_passaro + 30 > altura_obstaculo + espaco_entre_obstaculos:
            jogo_ativo = False

    # Preencher o fundo
    tela.fill(branco)

    # Desenhar o pássaro e os obstáculos
    desenhar_passaro(x_passaro, y_passaro)
    desenhar_obstaculo(x_obstaculo, altura_obstaculo)

    pygame.display.update()

    # Atraso de 30 milissegundos entre os quadros
    time.sleep(0.03)

# Finalização do Pygame
pygame.quit()
sys.exit()
