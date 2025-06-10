import pygame.transform
from Text import Text

from Entity import Entity
class Enemy(Entity):
    """Class representing an enemy in the game."""
    def __init__(self, name, max_health, armor, position=(0,0), image_path=None):
        super().__init__(max_health, armor, position=position, image_path=image_path, name=name)
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

    def create_hp_bar(self):
        if self.hp_bar is None:
            self.hp_bar = Text(
                text=f"{self._name} HP: {self._current_health}/{self.max_health}",
                position=(self.position[0]+100, self.position[1] + 220),
                font_size=20,
                color=(255, 255, 255),
                font_name="Fonts/Minecraft.ttf"
            )
            super().add_child(self.hp_bar)
        else:
            self.update_hp_bar()

    def update_hp_bar(self):
        self.hp_bar.text = f"{self._name} HP: {self._current_health}/{self.max_health}"

    def lose_health(self, value):
        super().lose_health(value)
        self.update_hp_bar()
