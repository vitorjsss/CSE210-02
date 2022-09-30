from cards import Cards

class Director:

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        cards = Cards()

        while self.is_playing:
            self.get_inputs(cards)
            self.do_updates(cards)
            self.do_outputs()

    def get_inputs(self, cards):
        """Gets the input from the user and run the play_cards function
        
        Args:
            self (Director): an instance of Director.
            cards (class): the Cards class created on cards.py
        """
        cards.play_cards()

    def do_updates(self, cards):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if cards.guess == 'h' and cards.next_card > cards.initial_card:
            self.score += 100
        elif cards.guess == 'l' and cards.next_card < cards.initial_card:
            self.score += 100
        else:
            self.score -= 75

    def do_outputs(self):
        """Displays the the score. Also asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """

        if not self.is_playing or self.score == 0:
            print('Game over')
            return
        
        print('Your score is: ',self.score)
        self.play_again = input('Play again? [y/n] ')
        while self.play_again != 'y' and self.play_again != 'n':
            print('Invalid Input!')
            self.play_again = input('Play again? [y/n] ')
        print()
        if self.play_again == 'n':
            self.is_playing = False