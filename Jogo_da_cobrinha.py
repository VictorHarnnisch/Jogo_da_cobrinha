import pygame
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Definir as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Definir as dimensões da cobrinha
TAMANHO_COBRA = 20
VELOCIDADE = 10

# Posição inicial da cobrinha
cobra_x = LARGURA // 2
cobra_y = ALTURA // 2
cobra = [(cobra_x, cobra_y)]

# Posição inicial da comida
comida_x = random.randint(0, LARGURA - TAMANHO_COBRA)
comida_y = random.randint(0, ALTURA - TAMANHO_COBRA)

# Direção inicial da cobrinha
direcao_x = TAMANHO_COBRA
direcao_y = 0

# Pontuação
pontuacao = 0

# Loop principal do jogo
rodando = True
while rodando:
    # Verificar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                direcao_x = -TAMANHO_COBRA
                direcao_y = 0
            elif evento.key == pygame.K_RIGHT:
                direcao_x = TAMANHO_COBRA
                direcao_y = 0
            elif evento.key == pygame.K_UP:
                direcao_x = 0
                direcao_y = -TAMANHO_COBRA
            elif evento.key == pygame.K_DOWN:
                direcao_x = 0
                direcao_y = TAMANHO_COBRA

    # Atualizar a posição da cabeça da cobrinha
    cobra_x += direcao_x
    cobra_y += direcao_y
    nova_cabeca = (cobra_x, cobra_y)
    cobra.append(nova_cabeca)

    # Verificar se a cobrinha comeu a comida
    if cobra_x == comida_x and cobra_y == comida_y:
        comida_x = random.randint(0, LARGURA - TAMANHO_COBRA)
        comida_y = random.randint(0, ALTURA - TAMANHO_COBRA)
        pontuacao += 1
    else:
        cobra.pop(0)

    # Verificar se a cobrinha bateu nas bordas
    if cobra_x < 0 or cobra_x >= LARGURA or cobra_y < 0 or cobra_y >= ALTURA:
        rodando = False

    # Verificar se a cobrinha bateu em si mesma
    if nova_cabeca in cobra[:-1]:
        rodando = False

    # Limpar a tela
    tela.fill(BRANCO)

    # Desenhar a cobrinha
    for segmento in cobra:
        pygame.draw.rect(tela, PRETO, (segmento[0], segmento[1], TAMANHO_COBRA, TAMANHO_COBRA))

    # Desenhar a comida
    pygame.draw.rect(tela, VERMELHO, (comida_x, comida_y, TAMANHO_COBRA, TAMANHO_COBRA))

    # Exibir a pontuação
    font = pygame.font.Font(None, 36)
    texto_pontuacao = font.render(f"Pontuação: {pontuacao}", True, PRETO)
    tela.blit(texto_pontuacao, (10, 10))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a velocidade do jogo
    pygame.time.Clock().tick(VELOCIDADE)

# Encerrar o Pygame
pygame.quit()