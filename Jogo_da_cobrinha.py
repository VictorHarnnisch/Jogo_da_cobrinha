import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

# Configurações da cobrinha
TAMANHO_COBRA = 20
VELOCIDADE_INICIAL = 8
VELOCIDADE_MAXIMA = 20
VELOCIDADE = VELOCIDADE_INICIAL
INCREMENTO_VELOCIDADE = 2

# Posição inicial da cobrinha
cobra_x = LARGURA // 2
cobra_y = ALTURA // 2
cobra = [(cobra_x, cobra_y)]

# Posição inicial da comida
comida_x = random.randrange(0, LARGURA - TAMANHO_COBRA + 1, TAMANHO_COBRA)
comida_y = random.randrange(0, ALTURA - TAMANHO_COBRA + 1, TAMANHO_COBRA)

# Direção inicial da cobrinha
direcao_x = TAMANHO_COBRA
direcao_y = 0

# Pontuação
pontuacao = 0

# Vidas
vidas = 3

# Fonte para texto
fonte = pygame.font.Font(None, 36)

# Loop principal do jogo
rodando = True
while rodando:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:  # Fecha a tela com a tecla ESC
                rodando = False
            elif evento.key == pygame.K_LEFT and direcao_x == 0:
                direcao_x = -TAMANHO_COBRA
                direcao_y = 0
            elif evento.key == pygame.K_RIGHT and direcao_x == 0:
                direcao_x = TAMANHO_COBRA
                direcao_y = 0
            elif evento.key == pygame.K_UP and direcao_y == 0:
                direcao_x = 0
                direcao_y = -TAMANHO_COBRA
            elif evento.key == pygame.K_DOWN and direcao_y == 0:
                direcao_x = 0
                direcao_y = TAMANHO_COBRA
            elif evento.key == pygame.K_SPACE:  # Aumenta a velocidade com a tecla espaço
                VELOCIDADE = min(VELOCIDADE_MAXIMA, VELOCIDADE + INCREMENTO_VELOCIDADE)
            elif evento.key == pygame.K_LALT or evento.key == pygame.K_RALT:  # Diminui a velocidade com a tecla ALT
                VELOCIDADE = max(2, VELOCIDADE - INCREMENTO_VELOCIDADE)

    # Atualiza a posição da cobrinha
    cobra_x += direcao_x
    cobra_y += direcao_y
    nova_cabeca = (cobra_x, cobra_y)
    cobra.append(nova_cabeca)

    # Verifica se a cobrinha comeu a comida
    if cobra[-1][0] == comida_x and cobra[-1][1] == comida_y:
        comida_x = random.randrange(0, LARGURA - TAMANHO_COBRA + 1, TAMANHO_COBRA)
        comida_y = random.randrange(0, ALTURA - TAMANHO_COBRA + 1, TAMANHO_COBRA)
        pontuacao += 1
    else:
        cobra.pop(0)

    # Verifica colisões com as bordas e com ela mesma
    if cobra_x < 0 or cobra_x >= LARGURA or cobra_y < 0 or cobra_y >= ALTURA or nova_cabeca in cobra[:-1]:
        vidas -= 1
        if vidas == 0:
            rodando = False
        else:
            cobra_x = LARGURA // 2
            cobra_y = ALTURA // 2
            cobra = [(cobra_x, cobra_y)]
            direcao_x = TAMANHO_COBRA
            direcao_y = 0

    # Desenha na tela
    tela.fill(PRETO)
    for segmento in cobra:
        pygame.draw.rect(tela, VERDE, (segmento[0], segmento[1], TAMANHO_COBRA, TAMANHO_COBRA))
    pygame.draw.rect(tela, VERMELHO, (comida_x, comida_y, TAMANHO_COBRA, TAMANHO_COBRA))

    # Exibe a pontuação, velocidade e vidas
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    texto_velocidade = fonte.render(f"Velocidade: {VELOCIDADE}", True, BRANCO)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, BRANCO)
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_velocidade, (10, 40))
    tela.blit(texto_vidas, (10, 70))

    # Atualiza a tela
    pygame.display.flip()

    # Controla a velocidade do jogo
    pygame.time.Clock().tick(VELOCIDADE)

# Encerra o Pygame
pygame.quit()