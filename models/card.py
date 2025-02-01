from models.suit import Suit


class Card:
    """
    Class representing a card of the english deck

    ...

    Attributes
    ----------
    __value: int
        An integer representing the value of the card
    __suit: Suit
        The suit of the card
    __rank: str
        A string representing the rank of the card

    Methods
    -------

    """

    def __init__(self, value: int, suit: Suit, rank: str):
        self.__value = value
        self.__suit = suit
        self.__rank = rank

    def get_value(self) -> int:
        return self.__value

    def get_suit(self) -> Suit:
        return self.__suit

    def get_rank(self) -> str:
        return self.__rank

    def set_value(self, value: int):
        self.__value = value

    def __str__(self) -> str:
        return f"{self.__rank} of {self.__suit.name}: Value {self.__value}"
