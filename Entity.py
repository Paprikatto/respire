import abc

from Animation import Animation
from Button import Button
from GameObject import GameObject
from ProgressBar import ProgressBar
from Text import Text


class Entity(abc.ABC, GameObject):

    def __init__(self, max_health, shield=0, position=(0, 0), image=None, hp_bar_offset: tuple[int, int] = (0, 100)):
        super().__init__(position, image)
        self.hp_text = None
        self.shield_widget = None
        self.hp_bar_widget = None
        self.hp_bar_offset = hp_bar_offset
        self._max_health = max_health
        self._current_health = max_health
        self._shield = shield
        self.create_hp_bar()
        self.dead = False
        self.damage_animation = Animation(
            ["Sprites/Slash/slash-anim-1.png","Sprites/Slash/slash-anim-2.png", "Sprites/Slash/slash-anim-3.png", "Sprites/Slash/slash-anim-4.png", "Sprites/Slash/slash-anim-5.png"],
            position = hp_bar_offset,
            scale=(3, 3)
        )
        self.add_child(self.damage_animation)

    def lose_health(self, value):
        if value < 0:
            raise ValueError("Amount must be non-negative")
        if self.shield > value:
            self.shield -= value
        else:
            value = value - self.shield
            self.shield = 0
            self._current_health -= value
        
        self.damage_animation.play()
        
        if self._current_health < 0:
            self._current_health = 0
        if self._current_health == 0:
            self.on_death()
        if hasattr(self.hp_bar_widget, "value"):
            self.hp_bar_widget.value = self.current_health
        if isinstance(self.hp_text, Text):
            self.hp_text.text = f"{self.current_health}/{self.max_health}"

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
        if isinstance(self.shield_widget, GameObject):
            self.shield_widget.visible = value != 0
            self.shield_widget.text = f"{self.shield}"
        else:
            print("shield widget not a game object")
        
    def gain_shield(self, value):
        self.shield += value
        
    def create_hp_bar(self):
        if self.image is None:
            raise ValueError("Image must be set before creating HP bar")
        self.hp_bar_widget = ProgressBar(
            position=(0 + self.hp_bar_offset[0], self.image.get_height() + self.hp_bar_offset[1]),
            value=self.current_health, 
            max_value=self._max_health
        )
        self.add_child(self.hp_bar_widget)
        self.shield_widget = Button(
                    position=(-self.hp_bar_widget.width // 2 - 10, 0),
                    height=20,
                    width=150,
                    background_color=(128, 128, 128),
                    text=f"{self.shield}",
                    font_size=22,
                    font_color=(0, 0, 0),
                    image="Sprites/armor_icon.png",
                    text_offset=(0, 5)
                )
        self.shield_widget.scale = (3, 3)
        self.hp_bar_widget.add_child(self.shield_widget)
        self.shield_widget.visible = self.shield > 0
        self.hp_text = Text(
            font_name="Fonts/Minecraft.ttf",
            font_size=20,
            text=f"{self.current_health}/{self.max_health}"
        )
        self.hp_bar_widget.add_child(self.hp_text)
    
    def on_death(self):
        self.visible = False
        print("Add on death function!")
        self.dead = True