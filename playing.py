import pygame
import time
import class_of_coins
import class_function_of_bucket
from class_of_text_and_image import *

dt = 0.05


def keyboard():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 1
        elif event.type == pygame.KEYDOWN:
            return 2
        return 0


def new_level_started(level, screen):
    """
    새로운 레벨이 시작될 때의 오프닝 화면을 보여줌
    :param level: 현재의 level (easy, medium, hard)
    :param screen: 출력할 스크린
    :return: 없음
    """
    text_new_level = Text('original', 30, level + '  모드를 시작합니다', 350, 200)
    text_give_life = Text('original', 15, '새로운 생명이 지급되었습니다!', 350, 300)
    life_image = Image("life.png", 335, 330, 30, 30)

    finished = False
    while not finished:
        if keyboard():
            finished = True

        screen.fill((255, 255, 255))
        text_new_level.screen_text_show(screen)
        if level is not 'easy':
            text_give_life.screen_text_show(screen)
            life_image.screen_image_show(screen)
        pygame.display.update()


def show_my_score(screen, text_show_money, list_of_life_image):
    """
    화면의 우측 상단에 현재 자신의 점수(획득한 금액)과 남은 생명 개수, 현재까지 진행 시간을 표시
    :param screen: 출력할 스크린
    :param text_show_money: 출력할 텍스트 객체 1
    :param list_of_life_image: 출력할 이미지 객체
    :return: 없음
    """
    text_show_money.screen_text_show(screen)
    for i in list_of_life_image:
        i.screen_image_show(screen)


def swing_show(player, coin):
    """
    진자 운동 과정을 화면에 출력함
    :param player: 플레이어 객체(화면에 점수를 표시하기 위해 전달함)
    :param coin: 진자 운동을 진행하는 동전 객체
    :return: bucket 객체
    """
    [coin_x, coin_v] = coin.coin_swing_init()
    [bucket_x, bucket_v, dx, t] = class_function_of_bucket.bucket_init(coin.level)     # t = 0, bucket 의 x, v, dx를 초기화
    bucket = class_function_of_bucket.Bucket(bucket_x, bucket_v, dx)     # bucket 객체를 이용해 bucket 관련 값 저장.

    text_show_money = Text('original', 20, '획득한 금액: ' + str(player.collected_money) + ' 원', 550, 50)
    list_of_life_image = []
    for i in range(player.life_left):
        list_of_life_image.append(Image("life.png", 650 - i * 35, 100, 25, 25))

    loop_flag = True
    while loop_flag:
        if keyboard() == 2:
            loop_flag = False
        coin.screen.fill((255, 255, 255))
        t = t + dt
        pygame.draw.line(coin.screen, (0, 0, 0), (10, 20), (700, 20), 10)  # 줄이 매달린 천장
        [coin_x, coin_v] = coin.coin_swing(coin_x, coin_v)
        bucket = class_function_of_bucket.bucket_location_movement(bucket, coin.screen, coin.level)
        show_my_score(coin.screen, text_show_money, list_of_life_image)

        pygame.time.delay(10)
        pygame.display.flip()
    coin.coin_swing_end(coin_x, coin_v)
    return bucket


def fall_show(player, coin, bucket):
    """
    동전의 포물선 운동 과정을 화면에 출력함
    :param player: 플레이어 객체(화면에 점수를 표시하기 위해 전달함)
    :param coin:
    :param bucket:
    :return: coin 과 bucket 의 최종 x 좌표값(각각 해서 2개의 리턴값)
    """
    t = 0
    loop_flag = True
    while loop_flag:
        if keyboard() == 2:
            loop_flag = False
        if 420 <= coin.image.loca_y + 15:   # 동전이 바구니에 들어가면 while 문 종료
            loop_flag = False
        t = t + dt
        coin.screen.fill((255, 255, 255))
        pygame.draw.line(coin.screen, (0, 0, 0), (10, 20), (700, 20), 10)  # 줄이 매달린 천장
        coin_x = coin.coin_falls(t, coin.v_x, coin.v_y)
        bucket = class_function_of_bucket.bucket_location_movement(bucket, coin.screen, coin.level)

        text_show_money = Text('original', 20, '획득한 금액: ' + str(player.collected_money) + ' 원', 550, 50)
        list_of_life_image = []
        for i in range(player.life_left):
            list_of_life_image.append(Image("life.png", 650 - i * 35, 100, 25, 25))
        show_my_score(coin.screen, text_show_money, list_of_life_image)
        pygame.time.delay(10)
        pygame.display.update()
        # pygame.display.flip()
    return coin_x, bucket.bucket_x


def did_coin_enter(coin_final_x, bucket_final_x):
    """
    동전이 bucket 에 들어갔는지를 판단하는 함수
    :param coin_final_x: 동전의 최종 위치
    :param bucket_final_x: bucket 의 최종 위치
    :return: 들어가면 True, 들어가지 않으면 False 리턴
    """
    bucket_w = 100
    if abs(coin_final_x - bucket_final_x) <= bucket_w / 2:
        print('yay')
        return True
    else:
        print('aww')
        return False


def basic_playing_flow(player, coin):
    """
        플레이의 전체적인 흐름을 진행하는 함수, 하나의 동전에 대한 함수
        :param player: 플레이어 객체
        :param coin: 플레이에 사용될 동전 객체
        :return: 게임이 종료되면(생명을 전부 소모하면) True 반환, 종료되지 않으면 False 반환
    """
    bucket = swing_show(player, coin)
    [coin_final_x, bucket_final_x] = fall_show(player, coin, bucket)

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
    new_level_started('easy', screen)
    for i in range(5):
        coin = class_of_coins.EasyCoin(easy_coin_cost, screen)
        print(player.life_left, player.collected_money)
        if basic_playing_flow(player, coin) is True:  # 이번 레벨을 수행하는 도중에 생명 5개 소진 했을 경우, True
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
    player.life_left = player.life_left + 1
    new_level_started('medium', screen)
    for i in range(5):
        coin = class_of_coins.MediumCoin(medium_coin_cost, screen)
        print(player.life_left, player.collected_money)
        if basic_playing_flow(player, coin) is True:
            return True
    return False


def hard_play(screen, player):
    """
        hard 모드에서의 게임 플레이를 진행하는 함수
        :param screen: 출력에 사용할 스크린
        :param player: 플레이어 객체
        :return: 도중 게임이 종료되면 True 반환, 종료되지 않으면 False 반환
    """
    hard_coin_cost = 500
    player.life_left = player.life_left + 1
    new_level_started('hard', screen)
    for i in range(5):
        coin = class_of_coins.HardCoin(hard_coin_cost, screen)
        print(player.life_left, player.collected_money)
        if basic_playing_flow(player, coin) is True:
            return True
    return False
