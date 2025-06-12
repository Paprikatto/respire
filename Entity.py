import abc

from Button import Button
from GameObject import GameObject
from ProgressBar import ProgressBar
from Text import Text

class Entity(abc.ABC, GameObject):

    def __init__(self, max_health, shield, position=(0, 0), image_path=None, name="Entity", hp_bar_offset: tuple[int, int] = (0, 100)):
        super().__init__(position, image_path)
        self.hp_bar_offset = hp_bar_offset
        self.hp_bar_widget = None
        self._max_health = max_health
        self._current_health = max_health
        self._shield = shield
        self._name = name
        self.create_hp_bar()

    def lose_health(self, value):
        if value < 0:
            raise ValueError("Amount must be non-negative")
        if self.shield > value:
            self.shield -= value
            return
        else:
            value = value - self.shield
            self.shield = 0
        self._current_health -= value
        if hasattr(self.hp_bar_widget, "value"):
            self.hp_bar_widget.value = self.current_health

    def gain_health(self, value):
        if value < 0:
            raise ValueError("Amount must be non-negative")
        if self._current_health + value > self._max_health:
            self._current_health = self._max_health
        else:
            self._current_health += value

    @property
    def max_health(self):
        return self._max_health
    @property
    def current_health(self):
        return self._current_health
    @property
    def shield(self):
        return self._shield
    @property
    def is_alive(self):
        return self._current_health > 0
    
    @current_health.setter
    def current_health(self, value):
        if value < 0:
            raise ValueError("Current health cannot be negative")
        if value > self._max_health:
            raise ValueError("Current health cannot exceed max health")
        self._current_health = value

    @max_health.setter
    def max_health(self, value):
        if value < 0:
            raise ValueError("Max health cannot be negative")
        self._max_health = value

    @shield.setter
    def shield(self, value):
        if value < 0:
            raise ValueError("Shield cannot be negative")
        self._shield = value
        
    def create_hp_bar(self):
        if self.image is None:
            raise ValueError("Image must be set before creating HP bar")
        self.hp_bar_widget = ProgressBar(position=(0 + self.hp_bar_offset[0], self.image.get_height() + self.hp_bar_offset[1]), value=self._max_health // 2, max_value=self._max_health)
        self.add_child(self.hp_bar_widget)
