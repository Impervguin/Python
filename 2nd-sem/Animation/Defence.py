import pygame
import os


def draw_porsh(surface, x, y):
    pygame.draw.rect(surface, (255, 255, 255), (x, y, 200, 50))
    pygame.draw.rect(surface, (255, 255, 255), (x + 75, y + 50 , 50, 200))

def draw_box(surface, x, y):
    pygame.draw.rect(surface, (255, 255, 255), (x, y, 200, 1000), 2)

def draw_baloon(surface, xc, yc, r, dr, n_p):
    pygame.draw.circle(surface, (255, 255, 255), (xc, yc), r + dr * N_punch)

def move_obj(x, y, vy , sec):
    return (x, y + vy * sec)


WIDTH = 1600
HEIGHT = 900
FPS = 60
VY = 1
VC = -3
DR = 10
R = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
xp, yp = 400, 400
xb, yb = 400, 400
xc, yc = 500, 250
N_m_punch = 7
N_punch = 0
porsh_moves = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    sec = clock.tick(FPS)
    screen.fill((0, 0, 0))
    draw_porsh(screen, xp, yp)
    draw_box(screen, xb, yb)
    draw_baloon(screen, xc, yc, R, DR, N_punch)
    if porsh_moves:
        xp, yp = move_obj(xp, yp, VY, sec)
        if yp > screen.get_size()[1]:
            yp = screen.get_size()[1]
            VY = -VY
        if yp < yb:
            VY = -VY
            N_punch += 1
            if N_punch >= N_m_punch:
                porsh_moves = 0
    else:
        xc, yc = move_obj(xc, yc, VC, sec)


    pygame.display.update()

