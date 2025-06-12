import interfaces


WIDTH = 1600
HEIGHT = 900
player = None
deck: interfaces.Deck | None = None
current_scene = None
mouse_position = (0,0)
main_font = None
enemies = None
pointing: bool = False
pointing_start: tuple[int, int] = (0, 0)
card: interfaces.Card | None = None  # Placeholder for Card class, to be set in main.py

