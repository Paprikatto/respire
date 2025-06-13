import pygame.transform
from Text import Text

from Entity import Entity
class Enemy(Entity):
    """Class representing an enemy in the game."""
    def __init__(self, max_health, shield, position=(0, 0), image_path=None, hp_bar_offset: tuple[int, int] = (0, 100)):
        super().__init__(max_health, shield, position=position, image_path=image_path, hp_bar_offset=hp_bar_offset)
        self.check_hover = True
        self._image = pygame.transform.flip(self._image, True, False)