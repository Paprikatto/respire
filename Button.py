
import pygame
from GameObject import GameObject
"""Klasa Button dziedziczy po GameObject i reprezentuje przycisk w grze.
   Przyjmuje pozycję, wysokość, szerokość i kolor tła jako argumenty.
   Do dodania do przycisku klasa Text, aby wyświetlić tekst na przycisku"""
class Button(GameObject):
    def __init__(self, position, height, width, background_color=(0,0,255)):
        super().__init__(position)
        self._height = height
        self._width = width
        self._background_color = background_color
        self._position = position
        self.rect = pygame.Rect(
            self._position[0],
            self._position[1],
            self._width,
            self._height
        )

    def render(self, screen):
        # self.rect.position = self.position
        pygame.draw.rect(screen, self._background_color, self.rect)





