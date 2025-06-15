from Scene import Scene
from Button import Button
from GameObject import GameObject
from Player import Player
from enemies import *
import globals
import pygame

from enemies import SkeletonSword


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.background_color = (0, 0, 0)
        self.background = Button(
            position=(globals.WIDTH // 2, globals.HEIGHT // 2),
            height=globals.HEIGHT,
            width=globals.WIDTH,
            image="Sprites/respire_background.png"
        )
        self.title = GameObject(image="Sprites/respire_logo.png", position=(globals.WIDTH // 2, globals.HEIGHT // 4))
        self.start_button = Button(
            position=(globals.WIDTH // 2, globals.HEIGHT // 2 - 25),
            height=50,
            width=200,
            background_color=(0, 0, 255),
            text="Start Game",
            font_size=30,
            font_color=(255, 255, 255),
            on_click=self.start_game
        )
        self.quit_button = Button(
            position=(globals.WIDTH // 2, globals.HEIGHT // 2 + 50),
            height=50,
            width=200,
            background_color=(255, 0, 0),
            text="Quit Game",
            font_size=30,
            font_color=(255, 255, 255),
            on_click= self.quit_game
        )
        self.add_object(self.background)
        self.add_object(self.title)
        self.add_object(self.start_button)
        self.add_object(self.quit_button)
        if globals.player is None:
            globals.player = Player(80,  position=(globals.WIDTH // 2 - 300, globals.HEIGHT // 2 + 100))

    @staticmethod
    def start_game():
        from BattleScene import BattleScene
        from RewardScene import RewardScene
        # if not hasattr(globals, "enemies") or globals.enemies is None:
        #     globals.enemies = [SkeletonSword(), SkeletonShield(), Shadow()]
        # globals.current_scene = BattleScene(globals.player, globals.enemies)
        # globals.current_scene.add_object(globals.player)
        globals.current_scene = RewardScene(globals.deck)

    @staticmethod
    def quit_game():
        pygame.quit()