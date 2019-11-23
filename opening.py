# pygame 사용법 출처 https://kkamikoon.tistory.com/129 [컴퓨터를 다루다]
# pygame 사용자 입력받기 https://code-examples.net/ko/q/2c3dbd7

import pygame
import class_of_player


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


def set_opening_screen_image():
    """
        기본 화면의 이미지 크기 및 위치 설정
        :param : 없음
        :return: 크기를 조정한 시작 화면의 이미지
    """
    coin_img = pygame.image.load("coin.png")
    treasure_img = pygame.image.load("treasure.png")
    coin_img_x = 50
    coin_img_y = 50
    treasure_img_x = 150
    treasure_img_y = 150
    coin_size_img = pygame.transform.scale(coin_img, (coin_img_x, coin_img_y))
    treasure_size_img = pygame.transform.scale(treasure_img, (treasure_img_x, treasure_img_y))
    return coin_size_img, treasure_size_img


def opening_screen_image_show(coin_size_img, treasure_size_img, screen):
    screen.blit(coin_size_img, (70, 80))
    screen.blit(coin_size_img, (120, 120))
    screen.blit(treasure_size_img, (60, 200))


def opening(screen):
    """
        오프닝 화면을 표시하고, 도중에 플레이어의 아이디를 입력받는 함수를 호출
        :param screen: 출력에 사용할 스크린
        :return: 아이디를 포함한 플레이어 객체
    """
    finished = False
    flag_id_input = False

    font_bold_size = 35
    font_original_size = 20
    font_bold = pygame.font.Font('a옛날사진관3.ttf', font_bold_size)
    font_original = pygame.font.Font('a옛날사진관2.ttf', font_original_size)

    text_title_obj = font_bold.render('하늘에서 동전이 떨어진다', True, (0, 0, 0))
    text_subtitle_obj = font_original.render('PRESS ANY KEY', True, (0, 0, 0))

    text_title = text_title_obj.get_rect()
    text_subtitle = text_subtitle_obj.get_rect()

    text_title.center = (450, 200)
    text_subtitle.center = (450, 300)

    (coin_size_img, treasure_size_img) = set_opening_screen_image()

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                flag_id_input = True

        screen.fill((255, 255, 255))
        opening_screen_image_show(coin_size_img, treasure_size_img, screen)
        screen.blit(text_title_obj, text_title)

        if flag_id_input is False:
            screen.blit(text_subtitle_obj, text_subtitle)
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

    (coin_size_img, treasure_size_img) = set_opening_screen_image()

    font_bold_size = 35
    font_original_size = 20

    font_bold = pygame.font.Font('a옛날사진관3.ttf', font_bold_size)
    font_original = pygame.font.Font('a옛날사진관2.ttf', font_original_size)

    text_title_obj = font_bold.render('하늘에서 동전이 떨어진다', True, (0, 0, 0))
    text_enter_id_obj = font_original.render('ENTER YOUR ID', True, (0, 0, 0))

    text_title = text_title_obj.get_rect()
    text_enter_id = text_enter_id_obj.get_rect()

    text_title.center = (450, 200)
    text_enter_id.center = (450, 260)

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

        text_player_id_obj = font_original.render(string_player_id, True, (0, 0, 0))
        text_player_id = text_player_id_obj.get_rect()
        text_player_id.center = (450, 300)

        screen.fill((255, 255, 255))
        opening_screen_image_show(coin_size_img, treasure_size_img, screen)
        screen.blit(text_title_obj, text_title)
        screen.blit(text_enter_id_obj, text_enter_id)
        screen.blit(text_player_id_obj, text_player_id)
        pygame.display.update()


def game_explain(screen, player_name):
    """
        게임에 대한 설명을 스크린에 표시함
        :param screen: 출력에 사용할 스크린
        :param player_name: 앞서 입력받은 플레이어의 아이디
        :return: 없음
    """
    font_original_size = 16
    #######
    font_original = pygame.font.Font('a옛날사진관2.ttf', font_original_size)

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
    text_explain_obj = []
    text_explain = []

    (coin_size_img, treasure_size_img) = set_opening_screen_image()

    for i in range(10):
        text_explain_obj.append(font_original.render(explanation[i], True, (0, 0, 0)))
        text_explain.append(text_explain_obj[i].get_rect())
        if i >= 1:
            text_explain[i].center = (450, 100 + 35*i)
        else:
            text_explain[i].center = (450, 90)

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                return
        screen.fill((255, 255, 255))
        opening_screen_image_show(coin_size_img, treasure_size_img, screen)
        for i in range(10):
            screen.blit(text_explain_obj[i], text_explain[i])

        pygame.display.update()