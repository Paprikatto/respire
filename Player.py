from Entity import Entity
class Player(Entity):
    """Class representing a player in the game."""
    def __init__(self, name, max_health, armor, position=(0,0)):
        super().__init__(max_health, armor, position=position, image_path="Sprites/werewolf-idle1.png")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

