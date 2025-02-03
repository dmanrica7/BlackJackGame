from models.card import Card
from models.suit import Suit
from random import shuffle


class Deck:
    """
    Class that represents the list of cards of an english deck

    ...

    Attributes
    ----------
    __cards: list
        The list of cards of the deck

    Methods
    -------

    shuffle
        It shuffles the list of cards

    draw: Card
        It removes the last element of the list of cards and returns it

    deal(num: int): list
        It takes {num} number of cards of the deck and returns them

    """

    def __init__(self):
        self.__cards = list()
        for card_suit in Suit:
            self.__cards.append(Card(1, card_suit, "A"))
            self.__cards.append(Card(2, card_suit, "2"))
            self.__cards.append(Card(3, card_suit, "3"))
            self.__cards.append(Card(4, card_suit, "4"))
            self.__cards.append(Card(5, card_suit, "5"))
            self.__cards.append(Card(6, card_suit, "6"))
            self.__cards.append(Card(7, card_suit, "7"))
            self.__cards.append(Card(8, card_suit, "8"))
            self.__cards.append(Card(9, card_suit, "9"))
            self.__cards.append(Card(10, card_suit, "10"))
            self.__cards.append(Card(10, card_suit, "J"))
            self.__cards.append(Card(10, card_suit, "Q"))
            self.__cards.append(Card(10, card_suit, "K"))
        shuffle(self.__cards)

    # Getter

    @property
    def cards(self) -> list:
        """
        Getter of the card list of the deck
        :return: list
            The list of cards
        """
        return self.__cards

    # Methods

    def shuffle(self):
        """
        Shuffles the list of cards
        :return: None
        """
        if len(self.__cards) > 0:
            shuffle(self.__cards)

    def draw(self) -> Card | None:
        """
        Gets a card from the deck, removes it and returns it
        :return: Card
            The card removed from the deck
        """
        if len(self.__cards) > 0:
            return self.__cards.pop()

    def deal(self, num: int) -> list:
        """
        Gets a number of cards from the deck, removes them and returns them
        :param num:  int
            The number of cards to get
        :return: list
            The list of cards removed from the deck
        """
        cards_dealt = []
        if len(self.__cards) >= num:
            for i in range(num):
                cards_dealt.append(self.__cards.pop())
        return cards_dealt
