import pygame


pygame.init()
size = (1000, 1000)
opening_screen = pygame.display.set_mode(size)
opening_screen.fill((255, 255, 255))

coin_img = pygame.image.load("coin.png")
treasure_img = pygame.image.load("treasure.png")
coin_img_x = 60
coin_img_y = 60
treasure_img_x = 300
treasure_img_y = 300

coin_size_img = pygame.transform.scale(coin_img, (coin_img_x, coin_img_y))
treasure_size_img = pygame.transform.scale(treasure_img, (treasure_img_x, treasure_img_y))

opening_screen.blit(coin_size_img, (100, 100))
opening_screen.blit(treasure_size_img, (700, 700))



