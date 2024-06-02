from core.commands import *
from core.player import Player
from core.game import Game
from core.decorators import init_map
from core.maps import read_map
import os
import time
from .main import play


def initialize() -> Game:
    os.system('clear')
    player = Player(0, 0)
    map = read_map('maps/exercise1.txt')
    init_map(map)
    game = Game(player, map)
    print("Original layout")
    game.print_map()
    time.sleep(1)
    return game

''' 
In exercise 1 students will explore:
    * move commands
    * change color command
    * exceptions
'''

game = initialize()
play(game)