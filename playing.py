import class_of_coins
from function_of_bucket import *


def keyboard():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 1
        if event.type == pygame.KEYDOWN:
            return 2


def swing_show(screen, coin, level):
    """
    :param screen:
    :param coin:
    :return: 없음
    """
    coin.coin_init()
    bucket_init(level)     # t = 0, bucket 의 x, v, dx를 초기화
    loop_flag = True
    while loop_flag:
        if keyboard() == 2:
            loop_flag = False
        pygame.draw.line(screen, (0, 0, 0), (10, 20), (700, 20), 10)  # 줄이 매달린 천장
        [coin_x, coin_v] = coin.coin_swing(coin_x, coin_v, screen)
        [bucket_x, bucket_v, dx] = bucket_location_movement(bucket_x, bucket_v, dx, screen, level)
        pygame.display.update()


def fall_show(screen, coin, bucket):
    """
    coin 클래스의 coin_swing 함수를 돌려서 매 순간 coin의 좌표를 받음
    bucket 클래스의 함수를 돌려서 매 순간 bucket의 좌표를 받음
    각 위치에 coin과 bucket 이미지를 출력함
    :param screen:
    :param coin:
    :param bucket:
    :return: coin과 bucket의 최종 x좌표값(각각 해서 2개의 리턴값)
    """
    loop_flag = True
    while loop_flag:
        if keyboard() == 2:
            loop_flag = False
        [x, y] = coin.coin_falls()
        bucket_x = bucket_location_movement(bucket_x)
        pygame.display.update()


def did_coin_enter(coin_final_x, bucket_final_x):
    """
    동전이 bucket에 들어갔는지를 판단하는 함수
    :param coin_final_x: 동전의 최종 위치
    :param bucket_final_x: bucket의 최종 위치
    :return: 들어가면 True, 들어가지 않으면 False 리턴
    """
    if abs((int(updatedX + neworiginX)) - (
            bucketX + bucket_w / 2)) <= bucket_w / 2:  # updatedX+neworiginX : 코인의 중심 X , bucketX + bucket_w/2 : bucket 중심 X
        print('yay')
        return True
    else:
        print('aww')
        return False


def basic_playing_flow(screen, player, coin, level):
    """
        플레이의 전체적인 흐름을 진행하는 함수, 하나의 동전에 대한 함수
        :param screen: 출력에 사용할 스크린
        :param player: 플레이어 객체
        :param coin: 플레이에 사용될 동전 객체
        :return: 게임이 종료되면(생명을 전부 소모하면) True 반환, 종료되지 않으면 False 반환
    """

    swing_show(screen, coin, bucket, level)
    fall_show()
    # (coin_final_x, bucket_final_x) = fall_show(screen, coin, bucket)

    if did_coin_enter(coin_final_x, bucket_final_x) is True:
        player.you_collected(coin.cost)
        return False
    else:
        return player.did_you_die()


def easy_play(screen, player):
    """
        easy 모드에서의 게임 플레이를 진행하는 함수
        :param screen: 출력에 사용할 스크린
        :param player: 플레이어 객체
        :return: 도중 게임이 종료되면 True 반환, 종료되지 않으면 False 반환
    """
    easy_coin_cost = 50
    for i in range(5):
        coin = class_of_coins.EasyCoin(easy_coin_cost)
        # bucket = class_of_buckets.EasyBucket() 이거 대신 bucket 위치 지정 함수로
        if basic_playing_flow(screen, player, coin, 'easy') is True:  # 파라미터에 나중에 bucket 추가할 것
            return True
    return False


def medium_play(screen, player):
    """
        medium 모드에서의 게임 플레이를 진행하는 함수
        :param screen: 출력에 사용할 스크린
        :param player: 플레이어 객체
        :return: 도중 게임이 종료되면 True 반환, 종료되지 않으면 False 반환
    """
    medium_coin_cost = 100
    for i in range(5):
        coin = class_of_coins.MediumCoin(medium_coin_cost)
        # bucket = class_of_buckets.MediumBucket() 이거 대신 bucket 위치 지정 함수로
        if basic_playing_flow(screen, player, coin, 'medium') is True: # 파라미터에 나중에 bucket 추가할 것
            return True
    return False


def hard_play(screen, player):
    """
        hard 모드에서의 게임 플레이를 진행하는 함수
        :param screen: 출력에 사용할 스크린
        :param player: 플레이어 객체
        :return: 도중 게임이 종료되면 True 반환, 종료되지 않으면 False 반환
    """
    medium_coin_cost = 500
    for i in range(5):
        coin = class_of_coins.HardCoin(hard_coin_cost)
        # bucket = class_of_buckets.HardBucket() 이거 대신 bucket 위치 지정 함수로
        if basic_playing_flow(screen, player, coin, 'hard') is True:  # 파라미터에 나중에 bucket 추가할 것
            return True
    return False
