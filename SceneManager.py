import random
import globals
from BattleScene import BattleScene
from Deck import Deck
from MainMenu import MainMenu
from RewardScene import RewardScene
from enemies import *


class SceneManager:
    def __init__(self):
        self.battle_index: int = -1
        if globals.scene_manager is None:
            globals.scene_manager = self
        globals.current_scene = MainMenu()
        
    def create_battle_scene(self) -> BattleScene:
        self.battle_index += 1
        # after 2 fights we fight 3 enemies instead of 2
        enemy_count = 3 if self.battle_index > 2 else 2
        # pick random classes
        enemy_classes = []
        for i in range(enemy_count):
            enemy_classes.append(random.randint(1, 3))
        # create enemy instances
        enemies = []
        for class_index in enemy_classes:
            match class_index:
                case 1:
                    enemies.append(SkeletonSword())
                case 2:
                    enemies.append(SkeletonShield())
                case 3:
                    enemies.append(Shadow())
        
        return BattleScene(globals.player, enemies)
        
    def create_reward_scene(self) -> RewardScene:
        return RewardScene()
    
    def on_battle_win(self):
        globals.current_scene = self.create_reward_scene()
        
    def start_battle(self):
        globals.current_scene = self.create_battle_scene()