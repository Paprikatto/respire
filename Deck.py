from typing import List
from Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self._deck = self.generate_starting_cards()
        self._hand = []
        self.draw(5)
        self.card_index_update()
        self._used_cards = []

    def card_index_update(self):
        for i, card in enumerate(self._hand):
            card.hand_index = i

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

    def draw(self, amount):
        drawn = []
        for _ in range(amount):
            card_index = random.randint(0, len(self._deck) - 1)
            drawn.append(self._deck.pop(card_index))
        self._hand += drawn

    def used(self, index):
        self._used_cards = self._deck.pop(index)
        self.draw(1)
        self.card_index_update()
