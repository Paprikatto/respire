from Entity import Entity
class Enemy(Entity):
    """Class representing an enemy in the game."""
    def __init__(self, name, max_health, armor):
        super().__init__(max_health, armor)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

