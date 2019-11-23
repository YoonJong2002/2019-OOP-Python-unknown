import pygame
import opening
import class_of_coins
import playing
list_of_players = []

pygame.init()

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
    player = opening.opening(screen)   # 여기서 하는게 뭐야??
    if playing.easy_play(screen, player) == False:
        break

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