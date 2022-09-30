import random

# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
"""A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

class Cards():    

# 2) Create the class constructor. Use the following method comment.
    """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
    """

    def __init__(self):
        self.guess = ''
        self.initial_card = 0
        self.next_card = 0

# 3) Create the roll(self) method. Use the following method comment.
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
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