import random
import globals
from BattleScene import BattleScene
from DeathScene import DeathScene
from MainMenu import MainMenu
from RewardScene import RewardScene
from SaveManager import SaveManager
from enemies import *



class SceneManager:
    def __init__(self):
        self.battle_index: int = -1
        if globals.scene_manager is None:
            globals.scene_manager = self
        globals.current_scene = MainMenu()
        SaveManager.get_instance().do_something()
        
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
        if SaveManager.get_instance().read("battle_index") is None or SaveManager.get_instance().read("battle_index") < self.battle_index+1:
            SaveManager.get_instance().save("battle_index", self.battle_index+1)
        
    def start_battle(self):
        globals.current_scene = self.create_battle_scene()

    def on_player_death(self):
        globals.current_scene = DeathScene()

