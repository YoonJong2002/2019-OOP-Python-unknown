import pygame
import time
import opening
import playing
import ending

list_of_players = []

pygame.init()

while True:
    screen = opening.set_screen()  # 기본 스크린 생성하여 screen에 저장
    player = opening.opening(screen)   # 오프닝 화면 띄우기, 플레이어 아이디 입력, 플레이어 객체 생성
    opening.game_explain(screen, player.player_name)

    start_time = time.time()
    is_game_over = False
    is_game_over = playing.easy_play(screen, player)
    if is_game_over is False:
        is_game_over = playing.medium_play(screen, player)
    if is_game_over is False:
        is_game_over = playing.hard_play(screen, player)
    end_time = time.time()
    player.time_spent = end_time - start_time

    list_of_players = ending.insert_player_in_list(player, list_of_players)
    ending.show_ranking(screen, list_of_players)
    if not ending.play_again(screen):
        break