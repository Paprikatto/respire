import abc
from GameObject import GameObject
from Text import Text

class Entity(abc.ABC, GameObject):

    def __init__(self, max_health, armor, position=(0,0), image_path=None, name="Entity"):
        super().__init__(position, image_path)
        self._max_health = max_health
        self._current_health = max_health
        self._armor = armor
        self._name = name

    def lose_health(self, value):
        if value < 0:
            raise ValueError("Amount must be non-negative")
        if value - self._armor < 0:
            return
        self._current_health -= value - self._armor

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
    def armor(self):
        return self._armor
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

    @armor.setter
    def armor(self, value):
        if value < 0:
            raise ValueError("Armor cannot be negative")
        self._armor = value
