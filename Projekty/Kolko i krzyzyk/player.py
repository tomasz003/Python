import math
import random

class Player:
    def __init__(self, letter):
        #letter: x or o
        self.letter=letter
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square=random.choice(game.available_moves())
        return square
    

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter +'\'s turn - input a number (0-8): ')
            #we're testing if it's integer and if it's free:
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square - try again.')
        
        return val