import pygame
from Card import Card
from Entity import Entity
from MainMenu import MainMenu
import globals
import warnings

from SaveManager import SaveManager
from SceneManager import SceneManager

warnings.filterwarnings("ignore")

pygame.init()
# load music
if not pygame.mixer.get_init():
    pygame.mixer.init()
pygame.mixer.music.load("Sounds/bg_music.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.2)
screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("Respire")
clock = pygame.time.Clock()
running = True
sm = SceneManager().get_instance()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if hasattr(sm.current_scene.hovered_item, "click"):
                    sm.current_scene.hovered_item.click()
        if event.type == pygame.MOUSEBUTTONUP:
            if globals.pointing: #cancel card pointing
                globals.pointing = False
                if isinstance(sm.current_scene.hovered_item, Entity):
                    globals.card.use(sm.current_scene.hovered_item)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    globals.mouse_position = pygame.mouse.get_pos()
    # rendering
    sm.current_scene.render(screen)
    
    #if pointing, draw a line from card to mouse position
    if globals.pointing and isinstance(globals.card, Card):
        pygame.draw.line(screen, "white", globals.card.global_position, globals.mouse_position, 5)
    # hovering logic
    hovered = sm.current_scene.hovered_item
    prev_hovered = sm.current_scene.prev_hovered_item
    if hovered != prev_hovered:
        if prev_hovered is not None:
            prev_hovered.on_hover_exit()
        if hovered is not None:
            hovered.on_hover_enter()

    sm.current_scene.prev_hovered_item = sm.current_scene.hovered_item
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
