from Scene import Scene
import globals
from GameObject import GameObject
from Text import Text
from Button import Button
from SaveManager import SaveManager
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
        self.survived_text = Text(
            position=(globals.WIDTH // 2, globals.HEIGHT // 4 + 60),
            text=f"You survived': {globals.scene_manager.battle_index} battles",
            font_size=20,
            color=(255, 255, 255),
        )
        self.current_record = Text(
            position=(globals.WIDTH // 2, globals.HEIGHT // 4 + 100),
            text=f"Current Record: {SaveManager.get_instance().read('battle_index')} battles",
            font_size=20,
            color=(255, 255, 255),
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
        self.add_object(self.survived_text)
        self.add_object(self.current_record)



    @staticmethod
    def quit_game():
        pygame.quit()