import pygame
import time
import pickle
import opening
import playing
import ending


def ranking_init():
    f = open('ranking', 'wb')
    pickle.dump([], f)
    f.close()


# ranking_init()  # 전체 랭킹을 초기화할 때만 사용

pygame.init()


while True:
    screen = opening.set_screen()  # 기본 스크린 생성하여 screen 에 저장
    player = opening.opening(screen)   # 오프닝 화면 띄우기, 플레이어 아이디 입력, 플레이어 객체 생성
    opening.game_explain(screen, player.player_name)  # 게임 설명 띄우기

    start_time = time.time()  # 시작 시간 측정(플레이 시간 측정에 활용)
    print("Game Start")
    is_game_over = False
    is_game_over = playing.easy_play(screen, player)  # easy 모드 플레이 실행
    if is_game_over is False:
        is_game_over = playing.medium_play(screen, player)  # easy 모드에서 게임오버되지 않은 경우, medium 모드 플레이 실행
    if is_game_over is False:
        is_game_over = playing.hard_play(screen, player)  # medium 모드에서 게임오버되지 않은 경우, hard 모드 플레이 실행
    end_time = time.time()  # 엔딩 시간 측정(플레이 시간 측정에 활용)
    player.time_spent = end_time - start_time  # 플레이 시간 계산

    (list_of_players, my_rank) = ending.insert_player_in_list(player)  # player 객체를 랭킹에 추가
    ending.show_ranking(screen, list_of_players, my_rank)  # 화면에 랭킹 보드 띄우기
    if not ending.play_again(screen):  # 다시 플레이할 것인지 확인
        break
