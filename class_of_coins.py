class BasicCoin:
    def __init__(self, cost, level):
        self.cost = cost
        self.level = level

    def coin_swing(self, screen):
        """
            함수의 기능 설명
            :param screen: 출력에 사용할 스크린
            :return: 없음(?????) 혹은 동전의 다음 x좌표, y좌표????
        """
        pass

    def coin_fall(self, screen):
        """
            함수의 기능 설명
            :param screen: 출력에 사용할 스크린
            :return: 없음(?????) 혹은 동전의 다음 x좌표, y좌표????
        """
        pass


class EasyCoin(BasicCoin):
    def __init__(self, cost):
        self.cost = cost
        # self.image = # 이미지 파일 삽입하는 방법 등..?


class MediumCoin(BasicCoin):
    def __init__(self, cost, level):
        self.cost = cost
        self.level = level
        # self.stringlength = 10 - level # 코드 돌려보면서 적절히 길이 조절 부탁!
        # self.image = # 이미지 파일 삽입하는 방법 등..?


class HardCoin(BasicCoin):
    def __init__(self, cost, level):
        self.cost = cost
        self.level = level
        # self.stringlength = 10 - level*2 # 얘도 코드 돌려보면서 길이 조절 부탁!
        # self.image = # 이미지 파일 삽입?