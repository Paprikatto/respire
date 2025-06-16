import pygame

import globals
import utils
from Button import Button
from Entity import Entity
from GameObject import GameObject
from pygame.math import Vector2



class Card(GameObject):
    ANIM_SPEED = 6
    HAND_WIDTH = round(globals.WIDTH * 0.5)
    DECK_POSITION = Vector2(-150, globals.HEIGHT - 100)
    USED_POSITION =  Vector2(globals.WIDTH + 50, globals.HEIGHT - 100)
    HOVER_Y_OFFSET = 50
    FONT_SIZE = 18
    def __init__(self, actions, energy_cost, use_on_player, card_image = None, sound = None, verbose = False):
        super().__init__(image="Sprites/card-template.png")
        self.scale = (3, 3)  # Scale the card image
        self.verbose = verbose
        self.visible = True
        self.actions = actions 
        self.energy_cost = energy_cost
        self.use_on_player = use_on_player
        self._target_position = (0,0)
        self.hand_index = -1 #-1 to deck, -2 to zużyta karta
        self.hand_size = 5
        self.animation_speed = 1
        self._on_click = self.on_click
        for t in self.generate_text():
            self.add_child(t)
        self.create_energy_widget()
        if card_image:
            _go = GameObject(image=card_image)
            _go.scale = (3, 3)
            self.add_child(_go)
        self.sound = sound
            
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
        dist = Vector2.distance_to(self.global_position, self._target_position)
        self.check_hover = dist < Card.ANIM_SPEED
        if not self.check_hover:
            dist = utils.clamp(dist, 60, 240) / 60
            move_vec = self._target_position - self.global_position
            move_vec = move_vec.normalize()
            move_vec *= Card.ANIM_SPEED * self.animation_speed * dist
            # self.global_position += move_vec
            self.global_position = self.global_position + move_vec
        else:
            self.global_position = self._target_position

    def use(self, target: Entity):
        from BattleScene import BattleScene
        from Enemy import Enemy
        from Player import Player
        if globals.player.energy < self.energy_cost:
            return
        if isinstance(target, Enemy) and self._use_on_player:
            return 
        if isinstance(target, Player) and not self.use_on_player:
            return
        globals.player.energy -= self.energy_cost
        # update energy text
        if isinstance(globals.current_scene, BattleScene):
            globals.current_scene.update_energy_text()
        if hasattr(self.sound, "play"):
            self.sound.play()
        
        print(f"using {self.actions} on {target}")
        # perform actions
        for action in self.actions.keys():
            if target is None:
                break
            match action:
                case "damage":
                    target.lose_health(self.actions[action])
                case "shield_player":
                    globals.player.gain_shield(self.actions[action])
                case "add_player_energy":
                    globals.player.add_energy(self.actions[action])
                case "damage_all":
                    if isinstance(globals.current_scene, BattleScene):
                        for enemy in globals.current_scene.enemies:
                            enemy.lose_health(self.actions[action])
                case "vulnerable":
                    target.add_vulnerable(self.actions[action])
                case "heal":
                    target.heal(self.actions[action])
                case "draw":
                    globals.deck.draw(self.actions[action])
                # case "upgrade":
                #     globals.deck.upgrade_hand(self.actions[action])
                case _:
                    raise ValueError(f"Unknown action: {action}")
        if globals.deck is not None:
            globals.deck.used(self.hand_index)
            
    def on_click(self):
        from RewardScene import RewardScene
        from SceneManager import SceneManager
        if self._hand_index != -3:  # if card is not reward card
            globals.pointing_start = self.global_position
            globals.pointing = True
        else:
            if isinstance(globals.current_scene, RewardScene) and isinstance(globals.scene_manager, SceneManager):
                globals.deck.add_card(self)
                globals.scene_manager.start_battle()
        globals.card = self
        
       
        
    def on_hover_enter(self):
        super().on_hover_enter()
        self._target_position -= Vector2(0, Card.HOVER_Y_OFFSET)
        self.animation_speed = 0.2
        
    def on_hover_exit(self):
        super().on_hover_exit()
        self._target_position += Vector2(0, Card.HOVER_Y_OFFSET)
        self.animation_speed = 1
    
    def generate_text(self):
        from Text import Text
        str = ""
        texts = []
        for action, value in self.actions.items():
            match action:
                case "damage":
                    str += f"Deal {value} damage\n"
                case "shield_player":
                    str += f"Gain {value} shield\n"
                case "add_player_energy":
                    str += f"Gain {value} energy\n"
                case "damage_all":
                    str += f"Deal {value} damage\nto all enemies\n"
                case "vulnerable":
                    str += f"Apply vulnerable\nfor {value} rounds\n"
                case "heal":
                    str += f"Heal {value}\n"
                case "draw":
                    str += f"Draw {value} cards\n"
                case "upgrade":
                    str += f"Upgrade {value} cards\n"
                case _:
                    raise ValueError(f"Unknown action: {action}")
        #iterate over every line in str and create a Text object for each line
        str = str.split("\n")
        for i, line in enumerate(str):
            l = line.strip()
            texts.append(Text((0, Card.FONT_SIZE * i), l, color=(0,0,0), font_size=Card.FONT_SIZE,font_name="Fonts/Minecraft.ttf"))
        return texts
    def create_energy_widget(self):
        widget = Button((0, 0), 20, 20,
                        text=f"{self.energy_cost}",
                        font_size=Card.FONT_SIZE,
                        font_color=(255, 255, 0),
                        image="Sprites/circle3.png",
                        )
        widget.scale = (3, 3)
        self.add_child(widget)
        widget.position = (-self.image.get_width() // 2 + 8, -self.image.get_height() // 2 + 8)

