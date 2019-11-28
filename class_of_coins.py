# 진자운동 참고 링크 https://pinkwink.kr/683
import pygame
import numpy as np
import random
from class_of_text_and_image import *
from pygame.locals import *

pen_fm = 0.01
pen_m = 0.1
pen_l = 100 * 0.01
pen_J = 0.02
pen_g = 9.8
gndCenterX = 350
gndCenterY = 20
penLength = pen_l * 100 * 2
updatedX = updatedY = 0


def keyboard():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 1
        if event.type == pygame.KEYDOWN:
            return 2


def calcODEFunc(x_val, v_val):
    return -pen_fm / (pen_m * pen_l * pen_l + pen_J) * v_val - pen_m * pen_g * pen_l / (pen_m * pen_l * pen_l + pen_J) * x_val


# Runge Kutta 미방 함수 구현하기, 이 함수를 링크에서 참조하였어요!
def solveODEusingRK4(x, v):
    dt = 0.05
    kx1 = v
    kv1 = calcODEFunc(x, v)

    kx2 = v + dt * kv1 / 2
    kv2 = calcODEFunc(x + dt * kx1 / 2, v + dt * kv1 / 2)

    kx3 = v + dt * kv2 / 2
    kv3 = calcODEFunc(x + dt * kx2 / 2, v + dt * kv2 / 2)

    kx4 = v + dt * kv3
    kv4 = calcODEFunc(x + dt * kx3, v + dt * kv3)

    dx = dt * (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
    dv = dt * (kv1 + 2 * kv2 + 2 * kv3 + kv4) / 6

    return x + dx, v + dv


class BasicCoin:
    def __init__(self, screen, cost, level):
        self.cost = cost
        self.level = level
        self.screen = screen
        self.image = Image("coin.png", 0, 0, 30, 30)
        self.neworiginX = 0
        self.neworiginY = 0
        self.v_x = 0
        self.v_y = 0

    def coin_swing_init(self):
        return 30 * np.pi / 180, 0  # 진자 운동의 x, v 초기화

    def coin_swing(self, x, v):
        """
        매 순간 코인의 좌표(x, y)를 받고 dt 이후의 x,y를 반환
        :param x:
        :param v:
        :return:
        """
        [x, v] = solveODEusingRK4(x, v)  # x 는 각변위
        self.image.loca_x = gndCenterX + self.stringlength * np.sin(x) - 15
        self.image.loca_y = gndCenterY + self.stringlength * np.cos(x) - 15
        self.image.screen_image_show(self.screen)
        pygame.draw.line(self.screen, (100, 100, 100), (gndCenterX, gndCenterY), (self.image.loca_x + 15, self.image.loca_y + 15), 2)  # 줄
        return x, v

    def coin_swing_end(self, x, v):
        """
        동전의 진자운동 변수를 포물선 운동에 쓰이는 변수로 변환.
        :param x: 진자운동 마지막의 각 위치
        :param v: 진자운동 마지막의 각 속도
        :return: 없음
        """
        self.neworiginX = gndCenterX + self.stringlength * np.sin(x)
        self.neworiginY = gndCenterY + self.stringlength * np.cos(x)
        self.v_x = self.stringlength * v * np.cos(-x)  # 줄을 끊은 순간에 동전의 속도
        self.v_y = self.stringlength * v * np.sin(-x)

    def coin_falls(self, t, v_x, v_y):
        """
        t 시간에, 동전의 위치를 계산하여 표시함
        """
        updatedX = v_x * t
        updatedY = v_y * t + 0.5 * 700 * t ** 2
        self.image.loca_x = self.neworiginX + updatedX - 15
        self.image.loca_y = self.neworiginY + updatedY - 15
        self.image.screen_image_show(self.screen)
        return self.neworiginX + updatedX


class EasyCoin(BasicCoin):
    def __init__(self, cost, screen):
        self.cost = cost
        self.screen = screen
        self.level = 'easy'
        self.stringlength = 300  # 코드 돌려보면서 적절히 쉬운 길이로 조절 부탁!
        self.image = Image("coin.png", 0, 0, 30, 30)
        self.neworiginX = 0
        self.neworiginY = 0
        self.v_x = 0
        self.v_y = 0


class MediumCoin(BasicCoin):
    def __init__(self, cost, screen):
        self.cost = cost
        self.screen = screen
        self.level = 'medium'
        self.stringlength = 250  # 코드 돌려보면서 적절히 쉬운 길이로 조절 부탁!
        self.image = Image("coin.png", 0, 0, 30, 30)
        self.neworiginX = 0
        self.neworiginY = 0
        self.v_x = 0
        self.v_y = 0


class HardCoin(BasicCoin):
    def __init__(self, cost, screen):
        self.cost = cost
        self.screen = screen
        self.level = 'hard'
        self.stringlength = 200  # 코드 돌려보면서 적절히 쉬운 길이로 조절 부탁!
        self.image = Image("coin.png", 0, 0, 30, 30)
        self.neworiginX = 0
        self.neworiginY = 0
        self.v_x = 0
        self.v_y = 0
