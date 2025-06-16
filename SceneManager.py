import random
import globals
from Deck import Deck
from DeathScene import DeathScene
from MainMenu import MainMenu
from RewardScene import RewardScene
from SaveManager import SaveManager
from BattleScene import BattleScene
from Scene import Scene
from Text import Text
from enemies import *
from typing import Type, Optional
from Player import Player



class SceneManager:
    _instance: Optional["SceneManager"] = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SceneManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.battle_index: int = -1
        self.current_scene: Scene = MainMenu()

    @classmethod
    def get_instance(cls: Type["SceneManager"]) -> "SceneManager":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
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
        self.current_scene = self.create_reward_scene()
        if SaveManager.get_instance().read("battle_index") is None or SaveManager.get_instance().read("battle_index") < self.battle_index:
            SaveManager.get_instance().save("battle_index", self.battle_index)
        
    def start_battle(self):
        self.current_scene = self.create_battle_scene()

    def on_player_death(self):
        self.current_scene = DeathScene()
        self.battle_index = -1

