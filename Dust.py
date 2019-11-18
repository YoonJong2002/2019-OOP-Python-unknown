import pygame
from pygame.locals import *
import numpy as np

coin_img = pygame.image.load('coin.png')
dt = 0.05
t = v = 0
x = 30 * np.pi / 180    # x는 rad단위
pen_fm = 0.01
pen_m = 0.1
pen_l = 100 * 0.01
pen_J = 0.02
pen_g = 9.8
gndCenterX = 150
gndConterY = 20
penLength = pen_l * 100 * 2


def calcODEFunc(tVal, xVal, vVal):
    return -pen_fm / (pen_m * pen_l * pen_l + pen_J) * vVal - pen_m * pen_g * pen_l / (
                pen_m * pen_l * pen_l + pen_J) * xVal


# Runge Kutta 미방 함수 구현하기
def solveODEusingRK4(t, x, v):
    kx1 = v
    kv1 = calcODEFunc(t, x, v)

    kx2 = v + dt * kv1 / 2
    kv2 = calcODEFunc(t + dt / 2, x + dt * kx1 / 2, v + dt * kv1 / 2)

    kx3 = v + dt * kv2 / 2
    kv3 = calcODEFunc(t + dt / 2, x + dt * kx2 / 2, v + dt * kv2 / 2)

    kx4 = v + dt * kv3
    kv4 = calcODEFunc(t + dt, x + dt * kx3, v + dt * kv3)

    dx = dt * (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
    dv = dt * (kv1 + 2 * kv2 + 2 * kv3 + kv4) / 6

    return x + dx, v + dv

pygame.init() #초기화

srf = pygame.display.set_mode((1000, 1000))

font = pygame.font.SysFont('Vernada.ttf', 25)
aurthorSrf = font.render('Thanks PinkWink', True, (50, 50, 50))


loopFlag = True

global updatedX, updatedY



while loopFlag:
    for event in pygame.event.get():  # 이 구문은 무엇일까?? 근데 없으면 안된다! :(
        if event.type == QUIT:
            loopFlag = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                loopFlag = False

    srf.fill((255, 255, 255))

    t = t + dt
    [x, v] = solveODEusingRK4(t, x, v)      # x 는 각변위
    print(x, v)
    updatedX = gndCenterX + penLength * np.sin(x)
    updatedY = gndConterY + penLength * np.cos(x)

    pygame.draw.line(srf, (100, 100, 100), (gndCenterX, gndConterY), (updatedX, updatedY), 2)
    pygame.draw.circle(srf, (100, 100, 100), (int(updatedX), int(updatedY)), 10, 0)
    pygame.draw.line(srf,(100,0,100),(int(updatedX), int(updatedY)), (int(updatedX+penLength*v*np.cos(-x)), int(updatedY+penLength*v*np.sin(-x))),2)

    pygame.draw.line(srf, (0, 0, 0), (10, 20), (290, 20), 10)

    pygame.time.delay(40)
    pygame.display.flip()
    srf.blit(coin_img,(100,100))
loopFlag = True
t = 0
v_x = penLength * v * np.cos(-x)
v_y = penLength * v * np.sin(-x)
neworiginX = updatedX
neworiginY = updatedY

while loopFlag:
    for event in pygame.event.get(): # 이 구문은 무엇일까?? 근데 없으면 안된다! :(
        if event.type == QUIT:
            loopFlag = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                loopFlag = False

    srf.fill((255, 255, 255))

    t = t + dt

    updatedX = v_x * t
    updatedY = v_y * t + 0.5 * 700 * t**2

    pygame.draw.circle(srf, (100, 100, 100), (int(updatedX + neworiginX), int(updatedY + neworiginY)), 10, 0)

    pygame.time.delay(40)
    pygame.display.flip()

