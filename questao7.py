# 7) Usando a biblioteca ‘pygame’, escreva um programa que desenha
# na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta),
# toda vez que a tecla espaço for pressionada ou o botão direito for clicado.

import pygame
from random import randint


BLACK = (0, 0, 0)
YELLOW = (255, 238, 0)

pygame.init()
DISPLAY = pygame.display.set_mode((800, 600), 0, 32)
DISPLAY.fill(BLACK)


def loop(func):

    # cria relogio
    clock = pygame.time.Clock()
    cont = 60

    finish = False

    while not finish:
      # Checar os eventos do mouse aqui:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    func()

        if cont == 60:
            cont = 0
        # Atualiza o desenho na tela
        pygame.display.update()
        # 60 frames por segundo
        clock.tick(60)
        cont += 1

def draw_square():
    DISPLAY.fill(BLACK)
    pygame.draw.rect(DISPLAY, YELLOW, (randint(0, 750), randint(0, 550), 50, 50))

#MAIN
loop(draw_square)