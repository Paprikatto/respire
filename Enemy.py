import pygame.transform
import globals

from Entity import Entity
from GameObject import GameObject
from Text import Text
import random
ACTION_IMAGES = {
    "damage": pygame.image.load("Sprites/card-sword.png"),
    "shield": pygame.image.load("Sprites/card-shield.png")
}
class EnemyAction:
    def __init__(self, name: str, value: int, weight: int):
        self.name = name
        self.value = value
        self.weight = weight
   
class ActionsWidget(GameObject):
    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.number_widget = Text(
            position = (-20, 20),
        )
        self.add_child(self.number_widget)

    @property
    def number(self):
        return self.number_widget.text

    @number.setter
    def number(self, value):
        self.number_widget.text = value

class Enemy(Entity):
    """Class representing an enemy in the game."""
    def __init__(self, max_health, shield, position=(0, 0), image=None, hp_bar_offset: tuple[int, int] = (0, 100)):
        super().__init__(max_health, shield, position=position, image=image, hp_bar_offset=hp_bar_offset)
        self.current_action: str = ""
        self.check_hover = True
        self._image = pygame.transform.flip(self._image, True, False)
        self.actions_values: dict[str, int] = {}
        self.actions: list[str] = []
        self.actions_widget: ActionsWidget = self.create_actions_widget()
        self.actions_widget.visible = False
        
    def set_actions(self, value: list[EnemyAction]):
        for a in value:
            self.actions_values[a.name] = a.value
            for i in range(a.weight):
                self.actions.append(a.name)
        
    # choose and show next action
    def request_action(self):
        if len(self.actions) == 0:
            raise ValueError(f"no actions on {self.__class__.__name__}")
        action = self.actions[random.randint(0, len(self.actions) - 1)]
        self.actions_widget.image = ACTION_IMAGES[action]
        self.actions_widget.scale = (2, 2)
        self.actions_widget.number = str(self.actions_values[action])
        self.actions_widget.visible = True
        self.current_action = action
        
    def perform_action(self):
        if self.dead:
            return 
        match self.current_action:
            case "damage":
                globals.player.lose_health(self.actions_values["damage"])
            case "shield":
                self.gain_shield(self.actions_values["shield"])
                
    
    def create_actions_widget(self) -> ActionsWidget:
        widget = ActionsWidget(
            position=(self.hp_bar_offset[0], -self.hp_bar_offset[1] - 50)
        )
        self.add_child(widget)
        return widget
    
    def on_end_player_turn(self):
        super().on_end_player_turn()
        
    def on_start_player_turn(self):
        super().on_start_player_turn()
        self.request_action()
        
        

        
        
        
    