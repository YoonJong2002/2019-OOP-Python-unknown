import pygame
import sys


def keyboard():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            return False
        elif event.type == pygame.KEYDOWN:
            return True
        else:
            return False
