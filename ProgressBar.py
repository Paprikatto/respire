import pygame

from Button import Button
from GameObject import GameObject


class ProgressBar(GameObject):
    def __init__(self, position = (0, 0), foreground_color=(255, 0, 0), background_color=(20, 20, 20),value = 50, max_value = 100, width=200, height=10):
        super().__init__(position)
        self.bg_bar = Button(
            position=(0, 0),
            height=height,
            width=width,
            background_color=background_color
        )
        self.add_child(self.bg_bar)
        self.fg_bar = Button(
            position=(0, 0),
            height=height,
            width=int(width * (value / max_value)),
            background_color=foreground_color
        )
        self.rect = pygame.Rect(
            self._position[0],
            self._position[1],
            width,
            height
        )
        self.rect.center = (self._position[0], self._position[1])
        self.add_child(self.fg_bar)
        self._value = 0
        self._max_value = max_value
        self.width = width
        self.height = height
        self.value = value
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if new_value < 0 or new_value > self._max_value:
            raise ValueError("Value must be between 0 and max_value")
        self._value = new_value
        self.fg_bar.width = self.width * (self._value / self._max_value)
        self.fg_bar.position = (-(self.bg_bar.width - self.fg_bar.width) // 2, 0)
        
    def render(self, screen):
        if not self.visible:
            return 
        for c in self.children:
            c.update_relative_position()
            c.render(screen)