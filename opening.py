# pygame 사용법 출처 https://kkamikoon.tistory.com/129 [컴퓨터를 다루다]
# pygame 사용자 입력받기 https://codeday.me/ko/qa/20190626/900396.html

import pygame

def set_screen():
    # 화면 기본 설정
    pygame.init()
    size = [700, 500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("하늘에서 동전이 떨어진다")
    return screen


def set_image():
    # 이미지 크기 및 위치 설정
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
    # 오프닝 화면 및 사용자 아이디 입력
    finished = False
    flag_id_input = False

    font_bold_size = 35
    font_original_size = 20
    font_bold = pygame.font.SysFont('a옛날사진관3', font_bold_size)
    font_original = pygame.font.SysFont('a옛날사진관2', font_original_size)

    text_title_obj = font_bold.render('하늘에서 동전이 떨어진다', True, (0, 0, 0))
    text_subtitle_obj = font_original.render('PRESS ANY KEY', True, (0, 0, 0))
    text_enter_id_obj = font_original.render('ENTER YOUR ID', True, (0, 0, 0))

    text_title = text_title_obj.get_rect()
    text_subtitle = text_subtitle_obj.get_rect()
    text_enter_id = text_enter_id_obj.get_rect()

    text_title.center = (450, 200)
    text_subtitle.center = (450, 300)
    text_enter_id.center = (450, 260)

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
            enter_id(screen)

        pygame.display.update()


def enter_id(screen):
    pass