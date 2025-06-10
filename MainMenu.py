from networkx.classes import selfloop_edges

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
            position=(0, 0),
            height=globals.HEIGHT,
            width=globals.WIDTH,
            image_path="Sprites/respire_background.png"
        )
        self.title = GameObject(image_path="Sprites/respire_logo.png", position=(globals.WIDTH // 2, globals.HEIGHT // 4))
        self.start_button = Button(
            position=(globals.WIDTH // 2 - 100, globals.HEIGHT // 2 - 25),
            height=50,
            width=200,
            background_color=(0, 0, 255),
            button_text="Start Game",
            font_size=30,
            font_color=(255, 255, 255),
            font_path="Fonts/Minecraft.ttf",
            on_click=self.start_game
        )
        self.quit_button = Button(
            position=(globals.WIDTH // 2 - 100, globals.HEIGHT // 2 + 50),
            height=50,
            width=200,
            background_color=(255, 0, 0),
            button_text="Quit Game",
            font_size=30,
            font_color=(255, 255, 255),
            font_path="Fonts/Minecraft.ttf",
            on_click= self.quit_game
        )
        self.player = Player("Player", 100, 10, position=(globals.WIDTH // 2 - 300, globals.HEIGHT // 2 + 100))
        self.add_object(self.background)
        self.add_object(self.title)
        self.add_object(self.start_button)
        self.add_object(self.quit_button)
        self.add_object(self.player)

    def start_game(self):
        from BattleScene import BattleScene
        from Player import Player
        from Enemy import Enemy
        import globals
        player = Player("Player", 100, 10)
        enemy = SkeletonSword()
        enemy2 = SkeletonShield()
        globals.current_scene = BattleScene(player, [enemy, enemy2])

    @staticmethod
    def quit_game():
        pygame.quit()