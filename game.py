from player import Player
from human import Human
from npc import Npc
from gestures import Gestures


class Game:
    def __init__(self):
        self.player_one = Human("player_one")
        self.player_two = Human("player_two")

    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.player_one_turn()
        self.player_two_turn()
        self.get_winner()
        self.display_winner()

    def display_welcome():
        print("welcome to my oop RPSLS game!")

    def choose_game_mode(self):
        print("How many players?")
        response = input()
        if response == 2:
            self.player_two = Human()
        else:
            self.player_two = Npc()

    def players(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def player_one_turn(self):
        print("Choose your gesture:")
        self.player_one.chosen_gesture = input()

    def player_two_turn(self):
        print("Choose your gesture:")
        self.player_two.chosen_gesture = input()

    def computer_turn(self):
        pass

    def display_winner(self):
        pass
