# Tu bedzie klasa Text
import pygame
from GameObject import GameObject

class Text(GameObject):
    def __init__(self, position, text, font_size=30, color=(255, 255, 255), font_name=None):
        super().__init__(position)
        self._text = text
        self._font_size = font_size
        self._color = color
        self._font_name = font_name if font_name else pygame.font.get_default_font()
        self._font = pygame.font.Font(self._font_name, self._font_size)
        self.image = self._font.render(self._text, True, self._color)
        self.rect = self.image.get_rect()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def render(self, screen):
        screen.blit(self.image, self.rect)
