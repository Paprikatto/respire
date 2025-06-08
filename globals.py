from Deck import Deck
from GameObject import GameObject
from Player import Player


WIDTH = 1280
HEIGHT = 720
player: Player | None = None
deck: Deck | None = None
mouse_position = (0,0)
main_font = None
hovered_item: GameObject | None = None
