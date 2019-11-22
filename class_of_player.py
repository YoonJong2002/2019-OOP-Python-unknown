class Player:
    def __init__(self, playername):
        self.playername = playername
        self.lifeleft = 5
        self.collectedmoney = 0
        self.timespent = 0

    def did_you_die(self):
        if self.lifeleft == 0:
            return True
        else:
            self.lifeleft = self.lifeleft - 1
            return False

    def you_collected(self, how_much_collected):
        self.collectedmoney = self.collectedmoney + how_much_collected
