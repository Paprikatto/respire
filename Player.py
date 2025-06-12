from Entity import Entity
from Text import Text
from Button import Button
class Player(Entity):
    """Class representing a player in the game."""
    def __init__(self, name, max_health, armor, position=(0,0)):
        super().__init__(max_health, armor, position=position, image_path="Sprites/Player/player.png", name="Player")
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
        self.energy = 5
        self.max_energy = 5
        self.energy_bar = None
        self.armor_bar = None
        self.vulnerability = 5
        self.vulnerability_bar = None
        self.create_hp_bar()
        self.create_armor_bar()
        self.create_vulnerability_bar()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def on_hover_enter(self):
        super().on_hover_enter()
        print("player hover enter")

    def on_hover_exit(self):
        super().on_hover_exit()
        print("player hover exit")

    def update(self):
        super().update()
        if self._is_idle:
            self._current_frame += 0.01
            if self._current_frame >= len(self._animation_list["idle"]):
                self._current_frame = 0
            self.image = self._idle_animation[int(self._current_frame)]
            self.scale = (5, 5)
        if self.hp_bar:
            # Ustaw pozycję względem globalnej pozycji gracza
            self.hp_bar.position = (self.global_position[0] - 20, self.global_position[1] - 150)
            self.update_hp_bar()
            if self.hp_bar not in self.children:
                super().add_child(self.hp_bar)


    def animate(self):
        self._is_idle = True

    def create_hp_bar(self):
        if self.hp_bar is None:
            self.hp_bar = Text(
                text=f"{self._name} HP: {self._current_health}/{self.max_health}",
                position=(self.position[0] - 20, self.position[1] - 150),
                font_size=20,
                color=(255, 255, 255),
                font_name="Fonts/Minecraft.ttf"
            )
            super().add_child(self.hp_bar)
        else:
            self.update_hp_bar()
            if self.hp_bar not in self.children:
                super().add_child(self.hp_bar)

    def update_hp_bar(self):
        self.hp_bar.text = f"{self._name} HP: {self._current_health}/{self.max_health}"

    def lose_health(self, value):
        super().lose_health(value)
        self.update_hp_bar()

    def create_armor_bar(self):
        if self.armor_bar is None and self.armor > 0:
            self.armor_bar = Button(
                position=(self.position[0] - 25, self.position[1] + 50),
                height=20,
                width=150,
                background_color=(128, 128, 128),
                button_text=f"{self.armor}",
                font_size=20,
                font_color=(0, 100, 0),
                font_path="Fonts/Minecraft.ttf",
                image_path="Sprites/armor_icon.png",
            )
            self.armor_bar.scale = (3, 3)
            self.armor_bar.text.position = (self.armor_bar.position[0], self.armor_bar.position[1] + 5)
            self.add_child(self.armor_bar)
        else:
            self.update_armor_bar()
            if self.armor_bar not in self.children:
                self.add_child(self.armor_bar)

    def update_armor_bar(self):
        self.armor_bar.text.text = f"{self.armor}"

    def create_vulnerability_bar(self):
        if self.vulnerability_bar is None:
            self.vulnerability_bar = Button(
                position=(self.position[0], self.position[1] + 50),
                height=20,
                width=150,
                background_color=(128, 128, 128),
                button_text=f"{self.vulnerability}",
                font_size=20,
                font_color=(100, 0, 0),
                font_path="Fonts/Minecraft.ttf",
                image_path="Sprites/armor_icon.png",
            )
            self.vulnerability_bar.scale = (3, 3)
            self.vulnerability_bar.text.position = (self.vulnerability_bar.position[0], self.vulnerability_bar.position[1] + 5)
            super().add_child(self.vulnerability_bar)
        else:
            self.update_vulnerability_bar()
            if self.vulnerability_bar not in self.children:
                super().add_child(self.vulnerability_bar)

    def update_vulnerability_bar(self):
        self.vulnerability_bar.text.text = f"{self.vulnerability}"
        if self.vulnerability > 0:
            self.vulnerability_bar.background_color = (255, 0, 0)