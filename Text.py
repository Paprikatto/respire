import pygame

import globals
from GameObject import GameObject

class Text(GameObject):
    def __init__(self, position: tuple[int, int] = (0, 0), text:str = "", font_size:int =30, color:tuple[int,int,int]=(255, 255, 255), font_name=None):
        super().__init__(position)
        self._text = text
        self._font_size = font_size
        self._color = color
        self._font_name = font_name if font_name else globals.default_font
        self._font = pygame.font.Font(self._font_name, self._font_size)
        self.image = self._font.render(self._text, True, self._color)
        self.rect = self.image.get_rect()
        self.rect.center = position

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.image = self._font.render(self._text, True, self._color)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
