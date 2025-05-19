import pygame

from Enemy import Enemy
from Player import Player
from Scene import Scene

#ta funkcja będzie usunięta ale na razie testuję
def setup_scene():
    """Set up the initial game scene."""
    # Initialize the scene
    scene = Scene()

    # Create game objects
    player = Player("Player", 100, 10, position=(100, 100))
    enemy = Enemy("Goblin", 50, 5, position=(300, 100), image_path="Sprites/werewolf-idle1.png")

    # Add objects to the scene
    scene.add_object(player)
    scene.add_object(enemy)

    return scene

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
scene1 = setup_scene()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    scene1.render(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
