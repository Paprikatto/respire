import pygame
from BattleScene import BattleScene
from Deck import Deck
from Enemy import Enemy
from MainMenu import MainMenu
from Player import Player
from Text import Text
import globals
import warnings
warnings.filterwarnings("ignore")

from Button import Button

#ta funkcja będzie usunięta ale na razie testuję
"""def setup_scene():
    # Initialize the scene
    player = Player("Player", 100, 10)
    player.scale = (5, 5)  
    enemy = Enemy("Goblin", 50, 5, image_path="Sprites/werewolf-idle1.png")
    enemy2 = Enemy("Goblin", 50, 5, image_path="Sprites/werewolf-idle1.png")
    enemy3 = Enemy("Goblin", 50, 5, image_path="Sprites/werewolf-idle1.png")
    enemy.scale = (5, 5)  
    enemy2.scale = (5, 5)  
    enemy3.scale = (5, 5)  
    scene = BattleScene(player, [enemy, enemy2, enemy3])
    # Add button
    button = Button((100, 100), 50, 200, background_color=(0, 255, 0), button_text="Attack", font_size=20, font_color=(0, 0, 0), font_path="Fonts/Minecraft.ttf")
    scene.add_object(button)


    return scene """

#Sprawdzam czy main menu działa
def setup_scene():
    # Initialize the scene
    scene = MainMenu()
    return scene

pygame.init()
globals.deck = Deck()
screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("Respire")
clock = pygame.time.Clock()
running = True

globals.current_scene = setup_scene()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if hasattr(globals.current_scene.hovered_item, "click"):
                    globals.current_scene.hovered_item.click()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    globals.mouse_position = pygame.mouse.get_pos()
    # RENDER YOUR GAME HERE
    globals.current_scene.render(screen)
    
    hovered = globals.current_scene.hovered_item
    prev_hovered = globals.current_scene.prev_hovered_item
    if hovered != prev_hovered:
        if prev_hovered is not None:
            prev_hovered.on_hover_exit()
        if hovered is not None:
            hovered.on_hover_enter()

    globals.current_scene.prev_hovered_item = globals.current_scene.hovered_item
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
