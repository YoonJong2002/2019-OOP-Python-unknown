import pygame
import time
import opening
import playing
import ending

list_of_players = []

pygame.init()

while True:
    screen = opening.set_screen()
    player = opening.opening(screen)   # 여기서 하는게 뭐야?? 오프닝 화면 띄우고, 사용자 아이디 입력받아서 객체로 저장!
    opening.game_explain(screen, player.player_name)

    start_time = time.time()
    is_game_over = False
    is_game_over = playing.easy_play(screen, player)
    if is_game_over is False:
        is_game_over = playing.medium_play(screen, player)
    if is_game_over is False:
        is_game_over = playing.hard_play(screen, player)

    ending.game_over(screen, player, list_of_players)
    if not ending.play_again(screen):
        break