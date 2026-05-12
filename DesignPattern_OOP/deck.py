import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck:
    new_deck = [Card(v, s) for s in ["C","Q","F","p"] for v in [range(14)]]
    def __init__(self):
        self.items = self.new_deck.copy()

    def shuffle(self) -> None:
        random.shuffle(self.items)
        pass

    def draw(self) -> Card:
        return self.items.pop()

    def reset(self) -> None:
        self.items = self.new_deck.copy()
        pass

    def __len__(self):
        return len(self.items)

    def __getitem__(self, n):
        return self.items[n]