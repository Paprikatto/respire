from typing import List
from Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self._deck = self.generate_starting_cards()
        self._hand = []
        self.draw(5)
        self._used_cards = []


    def generate_starting_cards(self) -> List:
        cards = []
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"damage": 5}, 2, False))
        cards.append(Card({"shield_player": 5}, 2, True))
        cards.append(Card({"shield_player": 5}, 2, True))
        cards.append(Card({"shield_player": 5}, 2, True))
        cards.append(Card({"shield_player": 5}, 2, True))
        cards.append(Card({"shield_player": 5}, 2, True))
        cards.append(Card({"shield_player": 5}, 2, True))
        cards.append(Card({"shield_player": 5}, 2, True))
        return cards

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
