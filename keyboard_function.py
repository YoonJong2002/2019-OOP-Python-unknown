import pygame


def keyboard():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 1
        elif event.type == pygame.KEYDOWN:
            return 2
        return 0