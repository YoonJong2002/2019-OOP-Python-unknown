class Player:
    def __init__(self, playername):
        self.playername = playername
        self.lifeleft = 5
        self.collectedmoney = 0

    def you_died(self):
        if self.lifeleft == 0:
            pass
        else:
            self.lifeleft = self.lifeleft - 1

    def you_collected(self, how_much_collected3):
        self.collectedmoney = self.collectedmoney + how_much_collected
