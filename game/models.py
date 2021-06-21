from abc import *


class AbstractCard(metaclass=ABCMeta):
    points: int
    suit: str
    value: int

    def stringify(self):
        return "{} of {}".format(self.value, self.suit)


class SUIT:
    SPADE = "♠️"
    HEART = "♥️"
    DIAMOND = "♦️"
    CLUB = "♣️"

    def __init__():
        pass


class RegularCard(AbstractCard):

    def __init__(self, suit: SUIT, value: int):
        self.suit = SUIT
        self.value = value


class SpecialCard(AbstractCard):
    """Special Cards

    - Ma hong, Das hund, Pheonix, Dragon
    """
    pass


CARD_VALUES = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}
