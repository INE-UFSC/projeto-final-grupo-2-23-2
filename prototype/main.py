import os
import sys

# reset the search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.game.game import Game

# start the game
if __name__ == '__main__': 
    game = Game()
    game.run()