class Card:
    points: int
    char: str


class RegularCard(Card):

    def __init__(suit, value):
        pass

    def to_string(self):
        return value + "of" + suit


char = {
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
    "Six": "6",
    "Seven": "7",
    "Eight": "8",
    "Nine": "9",
    "Ten": "10",
    "Jack": "J",
    "Queen": "Q",
    "King": "K",
    "Ace": "A"
}
