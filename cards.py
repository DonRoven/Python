class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "Card('{}', '{}')".format(self.rank, self.suit)


class Deck:
    _suits = ('spades', 'hearts', 'clubs', 'diamonds')
    _ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self):
        self._list = [Card(r, s) for r in self._ranks for s in self._suits]

    def draw(self):
        return self._list.pop()

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value
