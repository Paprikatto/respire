from typing import List

import pygame

import globals
from Card import Card
import random

if not pygame.mixer.get_init():
    pygame.mixer.init()
CARD_IMAGES = {
    "sword": pygame.image.load("Sprites/card-sword.png"),
    "shield": pygame.image.load("Sprites/card-shield.png")
}
CARD_SOUNDS = {
    "sword": pygame.mixer.Sound("Sounds/slice.wav"),
    "shield": pygame.mixer.Sound("Sounds/shield.mp3")
}
def generate_starting_cards() -> List:
    cards = []
    cards.append(Card({"damage": 5}, 1, False, CARD_IMAGES["sword"], CARD_SOUNDS["sword"]))
    cards.append(Card({"damage": 5}, 1, False, CARD_IMAGES["sword"], CARD_SOUNDS["sword"]))
    cards.append(Card({"damage": 5}, 1, False, CARD_IMAGES["sword"], CARD_SOUNDS["sword"]))
    cards.append(Card({"damage": 5}, 1, False, CARD_IMAGES["sword"], CARD_SOUNDS["sword"]))
    cards.append(Card({"damage": 11}, 2, False, CARD_IMAGES["sword"], CARD_SOUNDS["sword"]))
    cards.append(Card({"damage_all": 2}, 1, False, CARD_IMAGES["sword"], CARD_SOUNDS["sword"]))
    cards.append(Card({"damage_all": 2}, 1, False, CARD_IMAGES["sword"], CARD_SOUNDS["sword"]))
    cards.append(Card({"damage_all": 4}, 2, False, CARD_IMAGES["sword"], CARD_SOUNDS["sword"]))
    cards.append(Card({"shield_player": 5}, 2, True, CARD_IMAGES["shield"], CARD_SOUNDS["shield"]))
    cards.append(Card({"shield_player": 5}, 2, True, CARD_IMAGES["shield"], CARD_SOUNDS["shield"]))
    cards.append(Card({"shield_player": 5}, 1, True, CARD_IMAGES["shield"], CARD_SOUNDS["shield"]))
    cards.append(Card({"shield_player": 5}, 1, True, CARD_IMAGES["shield"],CARD_SOUNDS["shield"]))
    cards.append(Card({"shield_player": 5}, 1, True, CARD_IMAGES["shield"],CARD_SOUNDS["shield"]))
    return cards


class Deck:
    def __init__(self) -> None:
        self._deck = generate_starting_cards()
        self._hand = []
        self.draw(5)
        self._used_cards = []

    #draw {amount} cards from deck to hand
    def draw(self, amount):
        drawn = []
        for _ in range(amount):
            if len(self._deck) == 0:
                self.refill_deck()
            card_index = random.randint(0, len(self._deck) - 1)
            drawn.append(self._deck.pop(card_index))
        self._hand += drawn
        self.card_index_update()

    def refill_deck(self):
        for c in self._used_cards[:]: # kopia listy
            c.hand_index = -1
            self._used_cards.remove(c)
            self._deck.append(c)
    #give every card in hand an index
    def card_index_update(self):
        # self._hand[0].verbose = True
        hand_size = len(self._hand)
        for i, card in enumerate(self._hand):
            card.hand_index = i
            card.hand_size = hand_size

    #invoked in card class to delete certain card from hand and put it to used cards
    def used(self, index):
        c = self._hand.pop(index)
        c.hand_index = -2
        self._used_cards.append(c)
        self.draw(1)
        self.card_index_update()
    
    def render(self, screen):
        for card in self._hand:
            card.render(screen)
            card.update()
        for card in self._used_cards:
            if card.global_position != Card.USED_POSITION:
                card.render(screen)
                card.update()
        # Render hovered card second time to display it on top of others
        if isinstance(globals.current_scene.hovered_item, Card):
            globals.current_scene.hovered_item.render(screen)
            
            