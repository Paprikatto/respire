import globals
from GameObject import GameObject
from pygame.math import Vector2
class Card(GameObject):
    ANIM_SPEED = 15
    HAND_WIDTH = round(globals.WIDTH * 0.5)
    DECK_POSITION = Vector2(-50, globals.HEIGHT - 100)
    USED_POSITION =  Vector2(globals.WIDTH + 50, globals.HEIGHT - 100)
    def __init__(self, actions, energy_cost, use_on_player, verbose = False):
        super().__init__(image_path="Sprites/card-template.png")
        self.scale = (3, 3)  # Scale the card image
        self.verbose = verbose
        self.check_hover = True
        self.visible = True
        self.actions = actions 
        self.energy_cost = energy_cost
        self.use_on_player = use_on_player
        self._target_position = (0,0)
        self.hand_index = -1 #-1 to deck, -2 to zużyta karta
        self.hand_size = 5
        self._on_click = self.on_click
    
    @property
    def actions(self):
        return self._actions
    
    @actions.setter
    def actions(self, value):
        if not isinstance(value, dict):
            raise ValueError("Actions must be a dictionary")
        self._actions = value
    
    @property
    def energy_cost(self):
        return self._energy_cost
    
    @energy_cost.setter
    def energy_cost(self, value):
        if not isinstance(value, int):
            raise ValueError("Energy cost must be an integer")
        self._energy_cost = value
    
    @property
    def use_on_player(self):
        return self._use_on_player
    
    @use_on_player.setter
    def use_on_player(self, value):
        if not isinstance(value, bool):
            raise ValueError("Use on player must be a boolean")
        self._use_on_player = value
        
    @property
    def hand_index(self):
        return self._hand_index

    @hand_index.setter
    def hand_index(self, value: int):
        match value:
            case -2:
                self._target_position = Card.USED_POSITION
            case -1:
                self.global_position = Card.DECK_POSITION
                self._target_position = Card.DECK_POSITION
            case _:
                card_gap = Card.HAND_WIDTH // self.hand_size
                self._target_position = Vector2((value - 1) * card_gap + globals.WIDTH // 3, globals.HEIGHT - 50)

        self._hand_index = value

    def update(self):
        super().update()
        if self.verbose:
            print(self.global_position)
            print(self._target_position)
        if Vector2.distance_to(self.global_position, self._target_position) > Card.ANIM_SPEED:
            move_vec = self._target_position - self.global_position
            move_vec = move_vec.normalize()
            move_vec *= Card.ANIM_SPEED
            # self.global_position += move_vec
            self.global_position = self.global_position + move_vec
        else:
            self.global_position = self._target_position

    def use(self, target):
        for action in self.actions.keys():
            if target is None:
                break
            match action:
                case "damage":
                    target.take_damage(self.actions[action])
                case "shield_player":
                    globals.player.gain_shield(self.actions[action])
                case "add_player_energy":
                    globals.player.add_energy(self.actions[action])
                case "damage_all":
                    raise NotImplementedError("Damage all action is not implemented")
                case "vulnerable":
                    target.add_vulnerable(self.actions[action])
                case "heal":
                    target.heal(self.actions[action])
                case "draw":
                    globals.deck.draw(self.actions[action])
                case "upgrade":
                    globals.deck.upgrade_hand(self.actions[action])
                case _:
                    raise ValueError(f"Unknown action: {action}")
        if globals.deck is not None:
            globals.deck.used(self.hand_index)
            
    def on_click(self):
        self.use(None)
