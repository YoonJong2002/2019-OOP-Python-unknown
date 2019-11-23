import pygame
import opening


def game_over(screen, player, list_of_players):
    """
        게임이 종료되었을 때, list_of_players 의 적절한 위치에 플레이어를 삽입하고 랭킹을 화면에 표시함
        :param screen: 출력에 사용할 스크린
        :param player: 이번에 플레이한 플레이어 객체
        :param list_of_players: 이때까지 플레이한 플레이어 객체들의 리스트
        :return: 없음
    """
    pass


def play_again(screen):
    """
        사용자가 게임을 더 플레이할 것인지 물어봄
        :param screen: 출력에 사용할 스크린
        :return: 더 플레이한다면 True, 플레이하지 않는다면 False를 반환
    """
    font_original_size = 20
    font_original = pygame.font.SysFont('a옛날사진관2', font_original_size)
    text_ask_obj = font_original.render('다시 플레이하시겠습니까? (y or n)', True, (0, 0, 0))
    text_ask = text_ask_obj.get_rect()
    text_ask.center = (350, 250)

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                print(event.unicode.lower().startswith('y'))
                return event.unicode.lower().startswith('y')
        screen.fill((255, 255, 255))
        screen.blit(text_ask_obj, text_ask)
        pygame.display.update()


if __name__ == '__main__':
    screen = opening.set_screen()
    play_again(screen)