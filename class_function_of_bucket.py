import random
from class_of_text_and_image import *


def bucket_init(level):
    """
    바구니를 초기화(새로고침)함
    :param level: 단계 (easy, medium, hard)
    :return: 버킷의 초기 x, v, dx, 그리고 t를 0으로 초기화함
    """
    bucket_x = bucket_initial_location(level)  # 초기 x를 설정받음
    t = 0
    bucket_v = 0.5
    dx = bucket_v
    return bucket_x, bucket_v, dx, t


def bucket_initial_location(level):
    """
    하나의 동전을 던질 때마다 bucket 의 초기 위치를 돌려줌
    easy 인 경우 좁은범위에서 랜덤, 이외의 경우 조금 더 넓은 범위에서 랜덤
    :param level: easy / medium / hard
    :return: bucket 의 초기 x좌표
    """
    if level == 'easy':
        return random.randrange(150, 550)
    else:
        return random.randrange(50, 650)


def bucket_location_movement(Bucket, screen, level):
    """
    버킷의 움직임을 제어함
    :param Bucket: 버킷 객체, 버킷에 대한 변수가 담김
    :param screen: 화면의 이름
    :param level: 현재 난이도
    :return: 좌표가 바뀐 버킷을 반환
    """
    bucket_img = Image("bucket.png", Bucket.bucket_x, 420, 100, 80)

    if level == 'hard':
        if Bucket.bucket_x <= 50: # 왼쪽 끝에 도달했을때, 운동 방향 바뀜
            Bucket.dx = Bucket.bucket_v
        if Bucket.bucket_x >= 600: # 오른쪽 끝, 방향 바뀜
            Bucket.dx = -Bucket.bucket_v

        Bucket.bucket_x = Bucket.bucket_x + Bucket.dx      # 미소시간 dt 이후의 버킷 x 좌표
        bucket_img.loca_x = Bucket.bucket_x + Bucket.dx - bucket_img.size_x/2
        bucket_img.screen_image_show(screen)
        return Bucket
    else:   # easy, medium 에서는 버킷이 연속적으로 움직이지 않음
        bucket_img.loca_x = Bucket.bucket_x - bucket_img.size_x / 2
        bucket_img.screen_image_show(screen)
        return Bucket


class Bucket:
    """
    바구니와 관련된 변수를 저장
    """
    def __init__(self, x, v, dx):
        self.bucket_x = x
        self.bucket_v = v
        self.dx = dx
