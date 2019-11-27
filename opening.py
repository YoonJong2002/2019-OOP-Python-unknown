# pygame 사용법 출처 https://kkamikoon.tistory.com/129 [컴퓨터를 다루다]
# pygame 사용자 입력받기 https://code-examples.net/ko/q/2c3dbd7

import pygame
import class_of_player
from class_of_text_and_image import *


def set_screen():
    """
        기본적인 화면 설정
        :param : 없음
        :return: 기본 화면
    """
    pygame.init()
    size = [700, 500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("하늘에서 동전이 떨어진다")
    return screen


def opening(screen):
    """
        오프닝 화면을 표시하고, 도중에 플레이어의 아이디를 입력받는 함수를 호출
        :param screen: 출력에 사용할 스크린
        :return: 아이디를 포함한 플레이어 객체
    """
    finished = False
    flag_id_input = False

    text_title = Text('bold', 35, '하늘에서 동전이 떨어진다', 450, 200)
    text_subtitle = Text('original', 20, 'PRESS ANY KEY', 450, 300)

    coin_img_1 = Image("coin.png", 70, 80, 50, 50)
    coin_img_2 = Image("coin.png", 120, 120, 50, 50)
    treasure_img = Image("treasure.png", 60, 200, 150, 150)

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                flag_id_input = True

        screen.fill((255, 255, 255))

        text_title.screen_text_show(screen)
        coin_img_1.screen_image_show(screen)
        coin_img_2.screen_image_show(screen)
        treasure_img.screen_image_show(screen)

        if flag_id_input is False:
            text_subtitle.screen_text_show(screen)
        else:
            player_id = enter_id(screen)
            player = class_of_player.Player(player_id)
            return player

        pygame.display.update()


def enter_id(screen):
    """
        플레이어의 아이디를 입력받아 리턴함
        :param screen: 출력에 사용할 스크린
        :return: 입력받은 플레이어 아이디(문자열)
    """

    coin_img_1 = Image("coin.png", 70, 80, 50, 50)
    coin_img_2 = Image("coin.png", 120, 120, 50, 50)
    treasure_img = Image("treasure.png", 60, 200, 150, 150)
    text_title = Text('bold', 35, '하늘에서 동전이 떨어진다', 450, 200)
    text_enter_id = Text('original', 20, 'ENTER YOUR ID', 450, 260)

    string_player_id = ''

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(string_player_id) > 0:
                        return string_player_id
                elif event.key == pygame.K_BACKSPACE:
                    string_player_id = string_player_id[:-1]
                else:
                    string_player_id = string_player_id + event.unicode

        text_player_id = Text('original', 20, string_player_id, 450, 300)

        screen.fill((255, 255, 255))
        text_title.screen_text_show(screen)
        text_enter_id.screen_text_show(screen)
        text_player_id.screen_text_show(screen)
        coin_img_1.screen_image_show(screen)
        coin_img_2.screen_image_show(screen)
        treasure_img.screen_image_show(screen)

        pygame.display.update()


def game_explain(screen, player_name):
    """
        게임에 대한 설명을 스크린에 표시함
        :param screen: 출력에 사용할 스크린
        :param player_name: 앞서 입력받은 플레이어의 아이디
        :return: 없음
    """
    explanation = ["'하늘에서 동전이 떨어진다'에 오신 " + player_name + ", 환영합니다!",
                   "게임은 Easy, Medium, Hard의 세 가지 스테이지로 구성됩니다",
                   "동전은 실에 매달려 흔들리고,",
                   "Enter 키를 누르시면 줄이 끊겨 동전이 떨어집니다",
                   "아래쪽에 있는 양동이에 동전을 모으시면 성공입니다",
                   "실패하실 경우, 생명이 한 개씩 줄어듭니다",
                   "생명은 처음에 5개가 주어지고, ",
                   "각 스테이지를 통과하시면 하나씩 추가됩니다",
                   "최대한 많은 동전을 획득해보세요!",
                   "그럼, Good Luck!"]

    text_explain = []

    text_explain.append(Text('original', 16, explanation[0], 450, 90))
    for i in range(1, 10):
        text_explain.append(Text('original', 16, explanation[i], 450, 100 + 35 * i))
    coin_img_1 = Image("coin.png", 70, 80, 50, 50)
    coin_img_2 = Image("coin.png", 120, 120, 50, 50)
    treasure_img = Image("treasure.png", 60, 200, 150, 150)

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                return
        screen.fill((255, 255, 255))
        for i in range(10):
            text_explain[i].screen_text_show(screen)
        coin_img_1.screen_image_show(screen)
        coin_img_2.screen_image_show(screen)
        treasure_img.screen_image_show(screen)

        pygame.display.update()
    return
