import globals
class Card:
    def __init__(self, actions, energy_cost, use_on_player):
        self.actions = actions
        self.energy_cost = energy_cost
        self.use_on_player = use_on_player
        self.hand_index = -1
    
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
        
    def use(self, target):
        for action in self.actions.keys():
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
