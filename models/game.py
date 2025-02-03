from models.hand import Hand
from models.deck import Deck


class Game:
    """
    Class that represents a whole BlackJack game

    ...

    Attributes
    ----------
    __games_to_play: int
        Total games to play

    __game_number: int
        Current game number

    __deck: Deck
        List of cards

    __dealer_hand: Hand
        The hand of the dealer

    __player_hand: Hand
        The hand of the player

    Methods
    -------
    play: None
        Method to initialize the game

    __play_game: None
        Method that plays a single round of the game

    __check_winner(game_over: bool, optional): bool
        It the round isn't over, it checks if there's a winner already and if the game is over, it checks who won by points

    """

    def __init__(self):
        self.__games_to_play = 0
        self.__game_number = 0
        self.__deck = Deck()
        self.__dealer_hand = Hand(True)
        self.__player_hand = Hand(False)
        self.__bet = 0

    def play(self):
        player_score = 0
        dealer_score = 0
        while self.__games_to_play <= 0:
            try:
                self.__games_to_play = int(input("How many games do you want to play? "))
            except ValueError:
                print("You must enter an integer.")
            except TypeError:
                print("Something went wrong reading the input.")

        while self.__bet <= 0:
            try:
                self.__bet = int(input("How much do you want to bet in each round? "))
            except ValueError:
                print("You must enter an integer.")
            except TypeError:
                print("Something went wrong reading the input.")
        total_bet: float = self.__bet * self.__games_to_play
        print("Total bet:", total_bet)
        while self.__game_number < self.__games_to_play:
            self.__game_number += 1
            total_bet -= self.__bet
            winner, is_player_blackjack = self.__play_game()
            if winner == "player":
                if is_player_blackjack:
                    print(f"You get {self.__bet + self.__bet * 1.5}€ for the {self.__bet}€ of the bet")
                    total_bet += self.__bet + self.__bet * 1.5
                else:
                    print(f"You get {self.__bet * 2}€ for the {self.__bet}€ of the bet")
                    total_bet += self.__bet * 2
                player_score += 1
            elif winner == "dealer":
                print(f"You lose your {self.__bet}€")
                dealer_score += 1
            else:
                print(f"You get back your bet")
                total_bet += self.__bet
            self.__dealer_hand.clear()
            self.__player_hand.clear()
        print(f"\nPlayer's score: {player_score}\nDealer's score: {dealer_score}")
        if player_score < dealer_score:
            print("Dealer wins")
        elif player_score > dealer_score:
            print("You win")
        else:
            print("Tie")
        difference = total_bet - self.__bet * self.__games_to_play
        print(f"You {f'get {difference}' if difference >= 0 else f'lose {(-1)*difference}'}€")
        print("\nThanks for playing!")

    def __play_game(self) -> tuple:
        for _ in range(2):
            self.__player_hand.add_card(self.__deck.draw())
            self.__dealer_hand.add_card(self.__deck.draw())

        print(f"\nPlaying for {self.__bet}€")
        print("*" * 30)
        print(f"Game {self.__game_number} of {self.__games_to_play}")
        print("*" * 30)
        self.__dealer_hand.display()
        self.__player_hand.display()
        print()

        result = self.__check_winner()
        if result[0]:
            if result[1] == "player":
                return "player", self.__player_hand.is_blackjack()
            else:
                return result[1], False

        while self.__player_hand.get_value() < 21:
            choice = input("Choose 'Hit' or 'Stand', please (or 'h'/'s'): ").lower()
            if choice in ["hit", "h"]:
                self.__player_hand.add_card(self.__deck.draw())
                self.__player_hand.display()
            elif choice in ["stand", "s"]:
                break
            else:
                print("Incorrect answer.")

        result = self.__check_winner()
        if result[0]:
            if result[1] == "player":
                return "player", self.__player_hand.is_blackjack()
            else:
                return result[1], False

        while self.__dealer_hand.get_value() < 17:
            self.__dealer_hand.add_card(self.__deck.draw())
        self.__dealer_hand.display(True)

        result = self.__check_winner()
        if result[0]:
            return result[1], False

        print("Results:")
        print("Your hand:", self.__player_hand.get_value())
        print("Dealer's hand:", self.__dealer_hand.get_value())

        result = self.__check_winner(True)
        return result[1], False

    def __check_winner(self, game_over: bool = False) -> tuple:
        if not game_over:
            if self.__player_hand.get_value() > 21:
                print("You busted. Dealer wins! :(")
                return True, "dealer"
            elif self.__dealer_hand.get_value() > 21:
                print("Dealer busted. You win! :)")
                return True, "player"
            elif self.__dealer_hand.is_blackjack() and self.__player_hand.is_blackjack():
                print("Both players have blackjack! It's a tie!")
                return True, "tie"
            elif self.__player_hand.is_blackjack():
                print("You have a blackjack! You win! :)")
                return True, "player"
            elif self.__dealer_hand.is_blackjack():
                print("Dealer has a blackjack! Dealer wins! :(")
                return True, "dealer"
        else:
            if self.__player_hand.get_value() > self.__dealer_hand.get_value():
                print("You win! :)")
                return True, "player"
            elif self.__dealer_hand.get_value() == self.__player_hand.get_value():
                print("It's a tie.")
                return True, "tie"
            else:
                print("Dealer wins! :(")
                return True, "dealer"
        return False, ""
