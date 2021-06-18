from typing import Type, Union

from lizard import Lizard
from paper import Paper
from rock import Rock
from scissors import Scissors
from spock import Spock


class Player:
    def __init__(self):
        self.rock = Rock
        self.scissors = Scissors
        self.paper = Paper
        self.lizard = Lizard
        self.spock = Spock
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]

    def show_gestures(self):
        for single_gesture in self.gestures:
            print(single_gesture)

    def name_to_number(self):
        self = str.lower(self)
        if self == 'rock' or 'Rock':
            return 0
        elif self == 'spock' or 'Spock':
            return 1
        elif self == 'paper' or 'Paper':
            return 2
        elif self == 'lizard' or 'Lizard':
            return 3
        elif self == 'scissors' or 'Scissors':
            return 4
        else:
            print('ERROR: Name invalid')


    #def choose_gesture(self, player_2,):
