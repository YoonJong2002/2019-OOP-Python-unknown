import class_of_coins


def basic_playing_flow(screen, player, coin, v_x, v_y, x, y):
    """
        플레이의 전체적인 흐름을 진행하는 함수
        :param screen: 출력에 사용할 스크린
        :param coin: 플레이에 사용될 동전 객체
        :param x: (필요한가????)
        :param y: (필요한가????)
        :return: 게임이 종료되면 True 반환, 종료되지 않으면 False 반환
    """

    final_x, final_y = coin.coin_fall(screen)    # coin_fall 에 매개변수 추가하고 여기도 추가 필요!!

    if coin.did_coin_enter(final_x, final_y) is True:
        player.you_collected(coin.cost)
        return False
    else:
        return player.did_you_die()


def easy_play(screen, player):
    """
        easy 모드에서의 게임 플레이를 진행하는 함수
        :param screen: 출력에 사용할 스크린
        :param player: 플레이어 객체
        :return: 도중 게임이 종료되면 True 반환, 종료되지 않으면 False 반환
    """
    easy_coin_cost = 50
    for i in range(5):
        if player.did_you_die():
            return False    # 5개 던지기 전에 죽은 경우
        coin1 = class_of_coins.EasyCoin(easy_coin_cost, screen)
        coin1.coin_swings(screen)
        if coin1.coin_falls(screen):
            player.you_collected(easy_coin_cost)
        else :
            player.life_left -= 1

        print(player.life_left, player.collected_money)
    return True     # 5번 전부 던진 경우

def medium_play(screen, player):
    """
        medium 모드에서의 게임 플레이를 진행하는 함수
        :param screen: 출력에 사용할 스크린
        :param player: 플레이어 객체
        :return: 도중 게임이 종료되면 True 반환, 종료되지 않으면 False 반환
    """
    medium_coin_cost = 100
    for i in range(5):
        coin = class_of_coins.EasyCoin(medium_coin_cost)
        v_x, v_y, x, y = coin.coin_swing(screen, coin.stringlength)
        if basic_playing_flow(screen, player, coin, v_x, v_y, x, y) is True:
            return True
    return False


def hard_play(screen, player):
    """
        hard 모드에서의 게임 플레이를 진행하는 함수
        :param screen: 출력에 사용할 스크린
        :param player: 플레이어 객체
        :return: 도중 게임이 종료되면 True 반환, 종료되지 않으면 False 반환
    """
    hard_coin_cost = 500
    for i in range(5):
        coin = class_of_coins.EasyCoin(hard_coin_cost)
        v_x, v_y, x, y = coin.coin_swing(screen, coin.stringlength)
        if basic_playing_flow(screen, player, coin, v_x, v_y, x, y) is True:
            return True
    return False
