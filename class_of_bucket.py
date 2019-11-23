import pygame

bucket_w = 100
bucket_h = 80
bucket_img = pygame.image.load("bucket.png")
bucket_img_set = pygame.transform.scale(bucket_img, (bucket_h, bucket_w))


def bucket_moves(bucketX, bucket_v, dX):
    if bucketX <= 50:
        dX = bucket_v
    if bucketX >= 600:
        dX = -bucket_v

    bucketX = bucketX + dX
    bucketY = 450
    srf.blit(bucket_img_set, (bucketX, bucketY))
    pygame.display.update()
    return bucketX, bucket_v, dX


class bucket:
    def __init__(self, bucket_h, bucket_w):
        self.bucket_h = bucket_h
        self.bucket_w = bucket_w

    def bucket_move(self):
        while True:
            [bucketX, bucket_v, dX] = bucket_moves(bucketX, bucket_v, dX)  # bucket 의 이동.

bucket1 = bucket(80, 100)
bucket1.bucket_move()