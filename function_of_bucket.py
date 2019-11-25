import random
import pygame

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
    if level == 'hard':
        if bucket_x <= 50:
            dx = bucket_v
        if bucket_x >= 600:
            dx = -bucket_v
        bucket_x = bucket_x + dx
        bucket_y = 450
        screen.blit(bucket_img_set, (bucket_x, bucket_y))
        return bucket_x, bucket_v, dx
    else:
        return x

    # 범위 넘어가면 보정조건도 추가!!