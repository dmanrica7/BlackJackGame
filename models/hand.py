from models.card import Card


class Hand:
    """
    Class that represents the cards that a certain player has

    ...

    Attributes
    ----------

    __cards: list
        The list of cards that the player has

    __value: int
        The value of the cards that player has

    __dealer: bool
        Represents if the hand is from the dealer or not

    Methods
    -------

    add_card(Card)
        It appends the card passed by parameter to the hand

    add_cards(list)
        It appends the cards passed by parameter to the hand

    get_value: int
        It returns the value of the cards of the player

    is_dealer: bool
        It returns if the hand is from the dealer or from a player

    is_blackjack: bool
        It returns if the hand is a blackjack or not

    display: None
        Prints the hand in game

    clear: None
        Clears the hand for the next round
    """

    def __init__(self, dealer: bool):
        self.__cards = list()
        self.__value = 0
        self.__dealer = dealer

    def add_card(self, card: Card):
        """
        Add a card to the list of cards of the hand and updates the hand's value
        :param card: Card
            The card to add to the hand
        :return: None
        """
        if not self.__dealer:
            if card.get_rank() == "A":
                choice: int = 0
                while choice not in [1, 11]:
                    try:
                        choice = int(input("You've been dealt an A, which value do you want it to take? 1 or 11? "))
                    except ValueError:
                        print("Not a correct choice, try again")
                    except TypeError:
                        print("Something went wrong reading the input, try again")
                card.set_value(choice)

            for hand_card in self.__cards:
                if hand_card.get_rank() == "A":
                    choice: int = 0
                    while choice not in [1, 11]:
                        try:
                            print(f"Card dealt: {str(card)}")
                            choice = int(input("You had an A in your hand, which value do you want it to take? 1 or 11?"))
                        except ValueError:
                            print("Not a correct choice, try again")
                        except TypeError:
                            print("Something went wrong reading the input, try again")
                    self.__value += choice - hand_card.get_value()
                    hand_card.set_value(choice)
        else:
            if card.get_rank() == "A" and self.__value + 11 <= 21:
                card.set_value(11)

        self.__value += card.get_value()
        self.__cards.append(card)

    def get_value(self) -> int:
        """
        Gets the value of the hand
        :return: int
            The hand's value
        """
        return self.__value

    def is_dealer(self) -> bool:
        """
        Gets if the hand is from the dealer or not
        :return: bool
            True if the hand is from the dealer, False otherwise
        """
        return self.__dealer

    def is_blackjack(self) -> bool:
        """
        Gets if the value of the hand is equal to 21
        :return: bool
            True if the hand is a blackjack and False otherwise
        """
        return self.__value == 21

    def display(self, show_all_dealers_cards=False):
        """
        Prints the hand with its value
        :param show_all_dealers_cards: bool, optional
            False if the last dealer's card has to be hidden, True otherwise
        :return: None
        """
        if len(self.__cards) == 0:
            print(f'''{"Dealer's" if self.__dealer else "Your"} hand is empty''')
        else:
            print(f'''{"Dealer's" if self.__dealer else "Your"} hand:''')
            for index, card in enumerate(self.__cards):
                if index == 0 and self.__dealer and not show_all_dealers_cards and not self.is_blackjack():
                    print("\tHidden")
                else:
                    print(f"\t{str(card)}")
            print(f"Value: {'Hidden' if self.__dealer and not show_all_dealers_cards else self.__value}")

    def clear(self):
        """
        Removes all the cards and sets the value to zero
        :return: None
        """
        self.__cards.clear()
        self.__value = 0
