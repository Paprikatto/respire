from Entity import Entity
class Player(Entity):
    """Class representing a player in the game."""
    def __init__(self, name, max_health, armor, position=(0,0)):
        super().__init__(max_health, armor, position=position, image_path="Sprites/Player/player.png")
        self._idle_frame = 0
        self._name = name
        self.check_hover = True
        self._animation_list = {
            "idle": ["Sprites/Player/Idle/idle-with-weapon-1.png", "Sprites/Player/Idle/idle-with-weapon-2.png", "Sprites/Player/Idle/idle-with-weapon-3.png", "Sprites/Player/Idle/idle-with-weapon-4.png", "Sprites/Player/Idle/idle-with-weapon-5.png", "Sprites/Player/Idle/idle-with-weapon-6.png"],
        }
        self._idle_animation = self._animation_list["idle"]
        self.scale = (5, 5)
        self._current_frame = 0
        self._is_idle = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def on_hover_enter(self):
        print("player hover enter")

    def on_hover_exit(self):
        print("player hover exit")


    def update(self):
        super().update()
        if self._is_idle:
            self._current_frame += 0.01  # Adjust the speed of the animation here
            if self._current_frame >= len(self._animation_list["idle"]):
                self._current_frame = 0
            self.image = self._idle_animation[int(self._current_frame)]
            self.scale = (5, 5)


    def animate(self):
        self._is_idle = True

    def stop_animation(self):
        self._is_idle = False
        self._current_frame = 0
        self.image = self._idle_animation[self._current_frame]
        self.scale = (5, 5)