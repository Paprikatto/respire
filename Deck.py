from typing import List

import globals
from Card import Card
import random


def generate_starting_cards() -> List:
    cards = []
    cards.append(Card({"damage": 5}, 1, False))
    cards.append(Card({"damage": 5}, 2, False))
    cards.append(Card({"damage": 5}, 3, False))
    cards.append(Card({"damage": 5}, 4, False))
    cards.append(Card({"damage": 5}, 5, False))
    cards.append(Card({"vulnerable": 2}, 1, False))
    cards.append(Card({"vulnerable": 2}, 2, False))
    cards.append(Card({"vulnerable": 2}, 3, False))
    cards.append(Card({"vulnerable": 2}, 4, False))
    cards.append(Card({"vulnerable": 2}, 5, False))
    cards.append(Card({"shield_player": 5}, 1, True))
    cards.append(Card({"shield_player": 5}, 2, True))
    cards.append(Card({"shield_player": 5}, 3, True))
    cards.append(Card({"shield_player": 5}, 4, True))
    cards.append(Card({"shield_player": 5}, 5, True))
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
            card_index = random.randint(0, len(self._deck) - 1)
            drawn.append(self._deck.pop(card_index))
        self._hand += drawn
        self.card_index_update()

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
            
            