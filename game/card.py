DIAMOND = "diamond"
CLUB = "club"
HEART = "heart"
SPADE = "spade"
J = 11
Q = 12
K = 13
A = 14

SUITS = [DIAMOND, CLUB, HEART, SPADE]
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]

class Card:
    def __init__(self, suit, rank=None):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __repr__(self):
        return "Card('{}', {})".format(self.suit, self.rank)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rank == other
        else:
            return False

class Deck:
    def __init__(self):
        self.cards=[]

        # make 52 cards (without special cards)
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(Card(suit, rank))
        self.cards.append(Card("MahJong",1))
        self.cards.append(Card("Dog",0))
        self.cards.append(Card("Pheonix",1.5))
        self.cards.append(Card("Dragon",15))

    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def __repr__(self):
        return self.cards

    def __str__(self):
        return "Deck({})".format(len(self.cards))

    def __getitem__(self, item):
        return self.cards[item]