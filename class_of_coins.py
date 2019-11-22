class BasicCoin:
    def __init__(self, cost, level):
        self.cost = cost
        self.level = level

    def coin_swing(self, screen, stringlength):
        """
            실이 잘리기 전 동전의 진자운동을 구현
            :param screen: 출력에 사용할 스크린
            :return: 없음(?????) 혹은 동전의 다음 x좌표, y좌표????
        """
        pass

    def coin_fall(self, screen):
        """
            실이 잘린 후 동전의 포물선 운동을 구현
            :param screen: 출력에 사용할 스크린 # 필요에 따라 매개변수 추가 부탁!!!!
            :return: bucket과의 교점의 x좌표, y좌표(?????????) -> 충돌했는지 판단은 did_coin_enter
        """
        pass

    def did_coin_enter(self):
        """
            coin_fall 메서드에서 받은 매개변수를 이용하여 동전을 획득했는지 판단
            :param ?????????: 동전 획득 여부를 판단하니 위한 매개변수
            :return: 동전을 획득한 경우 True, 획득하지 못한 경우 Flase를 반환
        """
        pass


class EasyCoin(BasicCoin):
    def __init__(self, cost):
        self.cost = cost
        self.stringlength = 10  # 코드 돌려보면서 적절히 쉬운 길이로 조절 부탁!
        # self.image = # 이미지 파일 삽입하는 방법 등..?


class MediumCoin(BasicCoin):
    def __init__(self, cost, level):
        self.cost = cost
        self.level = level
        self.stringlength = 10 - level  # 코드 돌려보면서 적절히 길이 조절 부탁!
        # self.image = # 이미지 파일 삽입하는 방법 등..?


class HardCoin(BasicCoin):
    def __init__(self, cost, level):
        self.cost = cost
        self.level = level
        self.stringlength = 10 - level*2  # 얘도 코드 돌려보면서 길이 조절 부탁!
        # self.image = # 이미지 파일 삽입?
