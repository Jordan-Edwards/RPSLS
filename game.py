from human import Human
from npc import Npc


class Game:
    def __init__(self):
        self.game = Game


def display_welcome(self):
    print("welcome to my oop RPSLS game!")
    print()
    print("Scissors cuts Paper")
    print()
    print("Paper covers Rock")
    print()
    print("Rock crushes Lizard")
    print()
    print("Lizard poisons Spock")
    print()
    print("Spock smashes Scissors")
    print()
    print("Scissors decapitates Lizard")
    print()
    print("Lizard eats Paper")
    print()
    print("Paper disproves Spock")
    print()
    print("Spock vaporizes Rock")
    print()
    print("and as it always has, Rock crushes Scissors")

    player_one = Human()

    player_two_npc = Npc()

    self.choose_game_mode = int(input("enter a choice for Opponent (Computer 1, Human 2):"))
    if self.choose_game_mode == 1:
        print("Human vs Npc")
    elif not self.player_two_Npc == 2:
        print("Human vs Human")

    def round_loop(self):
       #round logic

