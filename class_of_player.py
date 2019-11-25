class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.life_left = 5
        self.collected_money = 0
        self.time_spent = 0


    def did_you_die(self):
        self.life_left = self.life_left - 1
        if self.life_left == 0:
            return True
        else:
            return False

    def you_collected(self, how_much_collected):
        self.collected_money = self.collected_money + how_much_collected

    def life_left_update(self):
        self.life_left -= 1

