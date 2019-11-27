import random
import pygame
from class_of_text_and_image import *


def bucket_init(level):
    bucket_x = bucket_initial_location(level)
    t = 0
    bucket_v = 0.5
    dx = bucket_v
    return bucket_x, bucket_v, dx, t


def bucket_initial_location(level):
    """
    하나의 동전을 던질 때마다 bucket 의 초기 위치를 돌려줌
    :param level: easy / medium / hard
    :return: bucket 의 초기 x좌표
    """
    if level == 'easy':
        return random.randrange(150, 550)
    else:
        return random.randrange(50, 650)


def bucket_location_movement(Bucket, screen, level):
    """
    hard 모드인 경우에만, dt가 지난 이후의 x좌표를 리턴해줌
    :param x: 처음 x좌표
    :return: dt 이후의 x좌표
    """

    bucket_img = Image("bucket.png", Bucket.bucket_x, 420, 100, 80)

    if level == 'hard':
        if Bucket.bucket_x <= 50:
            Bucket.dx = Bucket.bucket_v
        if Bucket.bucket_x >= 600:
            Bucket.dx = -Bucket.bucket_v
        bucket_img.loca_x = Bucket.bucket_x + Bucket.dx - bucket_img.size_x/2
        bucket_img.screen_image_show(screen)
        return Bucket
    else:
        bucket_img.loca_x = Bucket.bucket_x - bucket_img.size_x / 2
        bucket_img.screen_image_show(screen)
        return Bucket


class Bucket:
    def __init__(self, x, v, dx):
        self.bucket_x = x
        self.bucket_v = v
        self.dx = dx
