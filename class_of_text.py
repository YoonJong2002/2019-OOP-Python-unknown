import pygame

class Text:
    def __init__(self, font_size, font_text, font_x, font_y):
        self.font_size = font_size
        self.font_text = font_text
        self.font_x = font_x
        self.font_y = font_y



class BoldText(Text):
    boldfont = pygame.font.SysFont('a옛날사진관3', font_bold_size)
    # hihi

class OriginalText(Text):
    pass
