import pygame.mixer

from Entity import Entity
from Deck import CARD_SOUNDS
class Player(Entity):
    """Class representing a player in the game."""
    def __init__(self, max_health, shield = 0, position=(0, 0)):
        super().__init__(max_health, shield, position=position, image="Sprites/Player/player.png")
        self._idle_frame = 0
        self.check_hover = True
        self._animation_list = {
            "idle": ["Sprites/Player/Idle/idle-with-weapon-1.png", "Sprites/Player/Idle/idle-with-weapon-2.png", "Sprites/Player/Idle/idle-with-weapon-3.png", "Sprites/Player/Idle/idle-with-weapon-4.png", "Sprites/Player/Idle/idle-with-weapon-5.png", "Sprites/Player/Idle/idle-with-weapon-6.png"],
        }
        self._idle_animation = self._animation_list["idle"]
        self.scale = (5, 5)
        self._current_frame = 0
        self._is_idle = True
        self.hp_bar = None
        self.max_energy = 3
        self.energy = self.max_energy
        self.energy_bar = None
        self.armor_bar = None
        self.vulnerability = 5
        self.vulnerability_bar = None
        self.damage_sound = pygame.mixer.Sound(CARD_SOUNDS["sword"])
        self.damage_sound.set_volume(0.5)


    def lose_health(self, value):
        super().lose_health(value)
        self.damage_sound.play()
    def update(self):
        super().update()
        if self._is_idle:
            self._current_frame += 0.015
            if self._current_frame >= len(self._animation_list["idle"]):
                self._current_frame = 0
            self.image = self._idle_animation[int(self._current_frame)]
            self.scale = (5, 5)

    def animate(self):
        self._is_idle = True

    def on_end_player_turn(self):
        super().on_end_player_turn()

    def on_start_player_turn(self):
        super().on_start_player_turn()
        self.energy = self.max_energy