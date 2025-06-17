from Scene import Scene
from Button import Button
from Text import Text
from SaveManager import SaveManager
from GameObject import GameObject
from Player import Player
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
        self.background.scale = (1.5, 1.5)
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
        self.record_text = Text(
            position=(globals.WIDTH - 100, globals.HEIGHT - 25),
            text=f"Best Score: {SaveManager.get_instance().read('battle_index')}",
            font_size=20,
            color=(255, 255, 255),
        )
        self.add_object(self.background)
        self.add_object(self.title)
        self.add_object(self.start_button)
        self.add_object(self.quit_button)
        self.add_object(self.record_text)
        if globals.player is None:
            globals.player = Player(10,  position=(globals.WIDTH // 2 - 300, globals.HEIGHT // 2 + 100))

    @staticmethod
    def start_game():
        from SceneManager import SceneManager
        if isinstance(globals.scene_manager, SceneManager):
            globals.scene_manager.start_battle()

    @staticmethod
    def quit_game():
        pygame.quit()