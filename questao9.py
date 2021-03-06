# 9) Usando o código anterior, escreva um novo programa que, quando
# as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas,
# movimente o círculo com o texto “clique” nas direções corretas.
# Caso colida com algum retângulo, o retângulo que participou da colisão deve desaparecer.

import pygame, random, math
from pygame.locals import *

W = 800
H = 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
HOVER_COLOR = 50, 70, 90

RECT_LIST = []

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Questão 08 - Fund. Python - Mariana B. Sukevicz")
pygame.font.init()
clock = pygame.time.Clock()

running = True

CLOCK_TICK = 100

RAD = 100
RX = W // 2
RY = RAD
A = (RX, RY)


class Rectangle():
    def __init__(self):
        self.W = 60
        self.H = 30
        self.x = random.randint(0, W - self.W)
        self.y = random.randint(20, H - self.H)
        self.s_a = pygame.Rect(self.x, self.y, self.W, self.H)
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))

    def drawRectangle(self, screen):
        pygame.draw.rect(screen, self.color, self.s_a)


def drawCircle(RAD, RX, RY):
    pygame.draw.circle(screen, HOVER_COLOR, (RX, RY), RAD)
    font = pygame.font.SysFont('Times New Roman', 20)
    text = font.render("CLIQUE AQUI!", 1, WHITE)
    show_text = (RX - (RAD // 2), RY - 25)
    screen.blit(text, show_text)


def detectCollision(rleft, rtop, width, height, center_x, center_y, RAD):
    rright, rbottom = rleft + width / 2, rtop + height / 2
    cleft, ctop = center_x - RAD, center_y - RAD
    cright, cbottom = center_x + RAD, center_y + RAD
    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False

    for x in (rleft, rleft + width):
        for y in (rtop, rtop + height):
            if math.hypot(x - center_x, y - center_y) <= RAD:
                return True

    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True
    return False


while running:
    show = True
    screen.fill(WHITE)

    for c in RECT_LIST:
        c.drawRectangle(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            click = pygame.mouse.get_pos()
            collision_p = math.hypot(click[0] - RX, click[1] - RY)
            if collision_p <= RAD:
                r = Rectangle()
                r.drawRectangle(screen)
                for r_r in RECT_LIST:
                    if r_r.s_a.colliderect(r.s_a):
                        RECT_LIST.remove(r_r)
                        show = False
                if show:
                    RECT_LIST.append(r)

        keyboard = pygame.key.get_pressed()
        if keyboard[K_w]:
            RY -= 10
        elif keyboard[K_s]:
            RY += 10
        elif keyboard[K_a]:
            RX -= 10
        elif keyboard[K_d]:
            RX += 10

    circle = drawCircle(RAD, RX, RY)
    for c in RECT_LIST:
        if detectCollision(c.s_a.left, c.s_a.top, c.W, c.H, RX, RY, RAD):
            RECT_LIST.remove(c)

    pygame.display.update()
    clock.tick(CLOCK_TICK)

pygame.display.quit()
pygame.quit()