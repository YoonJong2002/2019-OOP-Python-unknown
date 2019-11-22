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


def set_image():
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
    font_bold = pygame.font.SysFont('a옛날사진관3', font_bold_size)
    font_original = pygame.font.SysFont('a옛날사진관2', font_original_size)

    text_title_obj = font_bold.render('하늘에서 동전이 떨어진다', True, (0, 0, 0))
    text_subtitle_obj = font_original.render('PRESS ANY KEY', True, (0, 0, 0))

    text_title = text_title_obj.get_rect()
    text_subtitle = text_subtitle_obj.get_rect()

    text_title.center = (450, 200)
    text_subtitle.center = (450, 300)

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                flag_id_input = True

        (coin_size_img, treasure_size_img) = set_image()

        screen.fill((255, 255, 255))
        screen.blit(coin_size_img, (70, 80))
        screen.blit(coin_size_img, (120, 120))
        screen.blit(treasure_size_img, (60, 200))
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
    # 사용자의 아이디를 입력받음
    font_bold_size = 35
    font_original_size = 20

    font_bold = pygame.font.SysFont('a옛날사진관3', font_bold_size)
    font_original = pygame.font.SysFont('a옛날사진관2', font_original_size)

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

        (coin_size_img, treasure_size_img) = set_image()
        text_player_id_obj = font_original.render(string_player_id, True, (0, 0, 0))
        text_player_id = text_player_id_obj.get_rect()
        text_player_id.center = (450, 300)

        screen.fill((255, 255, 255))
        screen.blit(coin_size_img, (70, 80))
        screen.blit(coin_size_img, (120, 120))
        screen.blit(treasure_size_img, (60, 200))
        screen.blit(text_title_obj, text_title)
        screen.blit(text_enter_id_obj, text_enter_id)
        screen.blit(text_player_id_obj, text_player_id)
        pygame.display.update()