import pygame
import pickle
import opening
from class_of_text_and_image import *
from keyboard_function import *


def insert_player_in_list(player):
    """
        게임이 종료되었을 때, list_of_players 의 적절한 위치에 플레이어를 삽입함
        :param player: 이번에 플레이한 플레이어 객체
        :return: player 을 삽입한 상태의 list_of_players
    """
    f = open('ranking', 'rb')
    list_of_players = pickle.load(f)
    f.close()
    list_of_players.append(player)
    list_of_players = sorted(list_of_players, reverse=True, key=lambda x: (x.collected_money, x.life_left, -x.time_spent))
    for i in list_of_players:
        if i == player:
            rank_index = list_of_players.index(player)
    f = open('ranking', 'wb')
    pickle.dump(list_of_players, f)
    f.close()
    return list_of_players, rank_index+1


def show_ranking(screen, list_of_players, my_rank):
    """
        정렬된 list of players 를 화면에 보여줌
        :param screen: 출력에 사용할 스크린
        :param list_of_players: 이때까지 플레이한 플레이어 객체들의 리스트
        :param my_rank: 방금 플레이한 플레이어의 랭킹
        :return: 없음
    """
    text_my_rank = Text('bold', 35, '당신의 랭킹은 ' + str(my_rank) + '위입니다!', 350, 50)
    text_rankings = [[Text('original', 20, '순위', 90, 110), Text('original', 20, 'ID', 190, 110),
                      Text('original', 20, '모은 금액(원)', 340, 110), Text('original', 20, '남은 생명', 460, 110),
                      Text('original', 20, '플레이 시간(초)', 600, 110)]]
    for i in range(min(len(list_of_players), 10)):
        text_rankings.append([Text('original', 20, str(i+1), 90, 140 + 30 * i),
                              Text('original', 20, list_of_players[i].player_name, 190, 140 + 30 * i),
                              Text('original', 20, str(list_of_players[i].collected_money), 340, 140 + 30 * i),
                              Text('original', 20, str(list_of_players[i].life_left), 460, 140 + 30 * i),
                              Text('original', 20, str(int(list_of_players[i].time_spent)), 600, 140 + 30 * i)])

    if my_rank <= 10:
        for i in text_rankings[my_rank]:
            i.font = pygame.font.Font('a옛날사진관3.ttf', i.font_size)
            i.obj = i.font.render(i.font_text, True, (255, 97, 3))
            i.text = i.obj.get_rect()
            i.text.center = (i.font_x, i.font_y)
    else:
        text_my_score = [Text('bold', 20, str(my_rank), 90, 450),
                         Text('bold', 20, list_of_players[my_rank-1].player_name, 190, 450),
                         Text('bold', 20, str(list_of_players[my_rank-1].collected_money), 340, 450),
                         Text('bold', 20, str(list_of_players[my_rank-1].life_left), 460, 450),
                         Text('bold', 20, str(int(list_of_players[my_rank-1].time_spent)), 600, 450)]

    while True:
        if keyboard() is True:
            return
        screen.fill((255, 255, 255))
        text_my_rank.screen_text_show(screen)
        for i in text_rankings:
            for j in i:
                j.screen_text_show(screen)
        if my_rank > 10:
            for i in text_my_score:
                i.screen_text_show(screen)

        pygame.display.update()


def play_again(screen):
    """
        사용자가 게임을 더 플레이할 것인지 물어봄
        :param screen: 출력에 사용할 스크린
        :return: 더 플레이한다면 True, 플레이하지 않는다면 False를 반환
    """
    text_ask = Text('original', 20, '다시 플레이하시겠습니까? (y or n)', 350, 250)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return event.unicode.lower().startswith('y')
        screen.fill((255, 255, 255))
        text_ask.screen_text_show(screen)
        pygame.display.update()


if __name__ == '__main__':
    screen = opening.set_screen()
    play_again(screen)
