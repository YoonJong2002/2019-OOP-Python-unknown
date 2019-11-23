import pygame


class Text:

    def __init__(self, what_font, font_size, font_text, font_x, font_y):
        self.font_size = font_size
        self.font_text = font_text
        self.font_x = font_x
        self.font_y = font_y

        if what_font == 'original':
            self.font = pygame.font.Font('a옛날사진관2.ttf', self.font_size)
        else:
            self.font = pygame.font.Font('a옛날사진관3.ttf', self.font_size)

        self.obj = self.font.render(self.font_text, True, (0, 0, 0))
        self.text = self.obj.get_rect()
        self.text.center = (font_x, font_y)

    def screen_text_show(self, screen):
        screen.blit(self.obj, self.text)
