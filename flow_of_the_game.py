import opening
import playing

list_of_players = []

while True:
    screen = opening.set_screen()
    player = opening.opening(screen)

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