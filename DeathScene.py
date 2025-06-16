from Scene import Scene
import globals
from GameObject import GameObject
from Text import Text
from Button import Button
import pygame

class DeathScene(Scene):
    def __init__(self):
        super().__init__()
        self.background_color = (0, 0, 0)
        self.background = GameObject(image="Sprites/respire_background.png", position=(globals.WIDTH // 2, globals.HEIGHT // 2))
        self.background.scale = (1.5, 1.5)

        self.title = Text(
            position=(globals.WIDTH // 2, globals.HEIGHT // 4),
            text="You Died",
            font_size=50,
            color=(255, 0, 0)
        )

        self.quit_button = Button(
            position=(globals.WIDTH // 2, globals.HEIGHT // 2 + 50),
            height=50,
            width=200,
            background_color=(255, 0, 0),
            text="Quit Game",
            font_size=30,
            font_color=(255, 255, 255),
            on_click=self.quit_game
        )

        self.add_object(self.background)
        self.add_object(self.title)
        self.add_object(self.quit_button)



    @staticmethod
    def quit_game():
        pygame.quit()