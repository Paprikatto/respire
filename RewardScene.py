from Card import Card
from Deck import Deck
from Text import Text
from pygame.math import Vector2
from Scene import Scene
import globals
import random
from cards import CARDS_DATA

class RewardScene(Scene):
    def __init__(self, deck: Deck):
        super().__init__()
        self.background_color = (0, 0, 0)
        self.deck = deck
        self.reward_text = Text(
            position=(globals.WIDTH // 2, globals.HEIGHT // 4),
            text="Choose your reward",
            font_size=40,
            color=(255, 255, 255),
            font_name="Fonts/Minecraft.ttf"
        )
        self.add_object(self.reward_text)
        self.reward_cards = []
        self.create_reward_cards()

    def create_reward_cards(self):
        import pygame
        chosen = random.sample(CARDS_DATA, 3)
        positions = [
            Vector2(globals.WIDTH // 4, globals.HEIGHT // 2),
            Vector2(globals.WIDTH // 2, globals.HEIGHT // 2),
            Vector2(globals.WIDTH // 4 * 3, globals.HEIGHT // 2)
        ]
        for i, card_data in enumerate(chosen):
            sound = pygame.mixer.Sound(card_data["sound_path"])
            reward_card = Card(
                card_data["actions"],
                card_data["energy_cost"],
                card_data["use_on_player"],
                card_data["image_path"],
                sound
            )
            reward_card.hand_index = -3  # Ustawienie indeksu karty w ręce na -3, aby nie była widoczna na dole ekranu
            reward_card.global_position = positions[i]  # Ustawienie pozycji kart
            reward_card._target_position = positions[i] # Ustawienie pozycji docelowej kart (target taki sam jak pozycja, aby nie było animacji)

            def on_click(new_card_data=card_data):
                new_card = Card(
                    new_card_data["actions"],
                    new_card_data["energy_cost"],
                    new_card_data["use_on_player"],
                    new_card_data["image_path"],
                    pygame.mixer.Sound(new_card_data["sound_path"])
                )
                self.deck.deck.append(new_card)

            reward_card.on_click = on_click
            self.add_object(reward_card)
            self.reward_cards.append(reward_card)

    def render(self, screen):
        screen.fill(self.background_color)
        for obj in self._game_objects:
            obj.render(screen)
        self.reward_text.render(screen)
        for card in self.reward_cards:
            card.update()
            card.render(screen)