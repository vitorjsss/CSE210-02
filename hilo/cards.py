import random

""" The responsibility of Cards is generate the random value of the card, ask the user guess
and show the value of the random card.
"""

class Cards():    

    """Constructs a new instance of Cards with a value and points attribute.

        Args:
            self (Cards): An instance of Cards.
    """
    def __init__(self):
        self.guess = ''
        self.initial_card = 0
        self.next_card = 0

    """Generates an initial random value for the first card, if it is the first time playing.
    If not, uses the value of the previous cards.
    Generates a new random value and gets the user's guess.
        
        Args:
            self (Cards): An instance of Cards.
    """
    def play_cards(self):
        if self.initial_card != 0:
            self.initial_card = self.next_card
        else:
            self.initial_card = random.randint(1,13)
        print('The card is: ',self.initial_card)
        self.guess = input("Higher or lower? [h/l] ")
        while self.guess != 'h' and self.guess != 'l':
            print('Invalid Input!')
            self.guess = input("Higher or lower? [h/l] ")
        self.next_card = random.randint(1,13)
        print('Next card was:', self.next_card)