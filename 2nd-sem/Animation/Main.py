import pygame
import os
from Classes import *

WIDTH = 1600
HEIGHT = 900
FPS = 60


BACKGROUND = pygame.image.load(os.path.join("Backgrounds", "back.jpg"))
PLANE = pygame.image.load(os.path.join("Sprites", "plane.png"))
PLANE_R = pygame.image.load(os.path.join("Sprites", "plane_r.png"))
BOMB = pygame.surface.Surface((20, 20))
BOMB.fill((0, 0, 0))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

plane = Plane(0, 600, 0, 20, 0.2, 0.5, PLANE)
planes = Objs(3, 3)
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(BACKGROUND, (0, 0))
    planes.draw(screen, PLANE, PLANE_R, BOMB)
    pygame.display.update()
    sec = clock.tick(FPS)
    planes.move(sec, screen)
    