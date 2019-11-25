import random


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


def bucket_location_movement(x):
    """
    hard 모드인 경우에만, dt가 지난 이후의 x좌표를 리턴해줌
    :param x: 처음 x좌표
    :return: dt 이후의 x좌표
    """
    pass
    # 범위 넘어가면 보정조건도 추가!!