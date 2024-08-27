import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(1, 5)] + list('JQKA')
    suits = 'Ravi Kumar'.split()

    def __init__(self):
        # self._cards = [Card(rank, suit) for suit in self.suits
        #                                 for rank in self.ranks]
        self.name='Ravi'
        self.araay=[1,2,3,4,5,6]

    def __len__(self):
        return len(self.name)
    
    def __getitem__(self, position):
        return self.araay[position]

def main():
    beer_card = Card('7', 'diamonds')
    # print(beer_card)

    deck = FrenchDeck()

    # __len__ usecase
    print(len(deck))
    # print(deck._cards)

    # __getitem__ usecase
    print(deck[-1])
    for card in deck:
        print(card)
    print( 2 in deck)
    # print( Card('Q', 'hearts') in deck)

    from random import choice
    print(choice(deck))

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    print(suit_values)

    rank_value = FrenchDeck.ranks.index(card.rank)

if __name__=="__main__":
    main()