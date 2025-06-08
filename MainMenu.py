from Scene import Scene
from Button import Button
from GameObject import GameObject
import globals
import pygame

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
        self.add_object(self.background)
        self.add_object(self.title)
        self.add_object(self.start_button)
        self.add_object(self.quit_button)

    def start_game(self):
        print("start")

    def quit_game(self):
        pygame.quit()
