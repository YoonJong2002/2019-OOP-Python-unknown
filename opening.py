# pygame 사용법 출처 https://kkamikoon.tistory.com/129 [컴퓨터를 다루다]
import pygame

pygame.init()

# 화면 기본 설정
size = [700, 500]
opening_screen = pygame.display.set_mode(size)
pygame.display.set_caption("하늘에서 동전이 떨어진다")

# 이미지 크기 및 위치 설정
coin_img = pygame.image.load("coin.png")
treasure_img = pygame.image.load("treasure.png")
coin_img_x = 50
coin_img_y = 50
treasure_img_x = 150
treasure_img_y = 150
coin_size_img = pygame.transform.scale(coin_img, (coin_img_x, coin_img_y))
treasure_size_img = pygame.transform.scale(treasure_img, (treasure_img_x, treasure_img_y))

# 폰트 및 출력 문구 설정
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


def opening():
    # 오프닝 화면 출력
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                finished = True

        opening_screen.fill((255, 255, 255))
        opening_screen.blit(coin_size_img, (70, 80))
        opening_screen.blit(coin_size_img, (120, 120))
        opening_screen.blit(treasure_size_img, (60, 200))
        opening_screen.blit(text_title_obj, text_title)
        opening_screen.blit(text_subtitle_obj, text_subtitle)
        pygame.display.update()

def enter_id():
    pass