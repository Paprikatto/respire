import pygame.transform
from Text import Text

from Entity import Entity
class Enemy(Entity):
    """Class representing an enemy in the game."""
    def __init__(self, name, max_health, shield, position=(0, 0), image_path=None, hp_bar_offset: tuple[int, int] = (0, 100)):
        super().__init__(max_health, shield, position=position, image_path=image_path, name=name, hp_bar_offset=hp_bar_offset)
        self._image = pygame.transform.flip(self._image, True, False)
        self.hp_bar = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value
