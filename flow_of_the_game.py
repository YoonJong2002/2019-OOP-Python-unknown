import pygame
import opening
import class_of_coins
import Dust

list_of_players = []

def keyboard():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 1
        if event.type == pygame.KEYDOWN:
            return 2

MainLoop = True
while MainLoop:
    if keyboard() == 1:
        MainLoop = False
    screen = opening.set_screen()
    player = opening.opening(screen) # 여기서 하는게 뭐야??
    coin1 = class_of_coins.EasyCoin(100, screen) # Easy mode 의 100원 짜리 동전 생성
    coin1.coin_swings(screen)
    coin1.coin_falls(screen)




    """
    is_game_over = False
    is_game_over = playing.easy_play(screen, player)
    if is_game_over is False:
        is_game_over = playing.medium_play(screen, player)
    if is_game_over is False:
        is_game_over = playing.hard_play(screen, player)
    """
    # ending.game_over()

    # list_of_players.append(player)

    # if not play_again():
        # break