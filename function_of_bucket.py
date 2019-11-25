import random
import pygame
import class_of_text_and_image

def bucket_init(level):
    global bucket_x
    bucket_x = bucket_initial_location(level)
    t = 0
    bucket_v = 0.5
    dx  = bucket_v

def bucket_initial_location(level):
    """
    하나의 동전을 던질 때마다 bucket의 초기 위치를 돌려줌
    :param level: easy / medium / hard
    :return: bucket의 초기 x좌표
    """
    if level == 'easy':
        return random.randrange(150, 650)
    else:
        return random.randrange(50, 750)


def bucket_location_movement(bucket_x, bucket_v, dx, screen, level):
    """
    hard 모드인 경우에만, dt가 지난 이후의 x좌표를 리턴해줌
    :param x: 처음 x좌표
    :return: dt 이후의 x좌표
    """

    bucket_img = class_of_text_and_image.Image("bucket.png", bucket_x, 450, 100, 80)

    if level == 'hard':
        if bucket_x <= 50:
            dx = bucket_v
        if bucket_x >= 600:
            dx = -bucket_v
        bucket_img.loca_x = bucket_x + dx
        bucket_img.screen_image_show(screen)
        return bucket_x, bucket_v, dx
    else:
        return bucket_x

    # 범위 넘어가면 보정조건도 추가!!