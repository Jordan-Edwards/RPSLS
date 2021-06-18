from human import Human
from npc import Npc
import time
from player import Player


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        time.sleep(1)
        print()
        self.player_one.name = input("What is your name?")
        print()
        print(
            f"Welcome {self.player_one.name}, to Rock, Paper, Scissors, Lizard, Spock popularized by 'The Big Bang Theory'!")
        print()
        print()
        self.game_rules()
        print()
        print("Now to select your game mode.")
        self.choose_game_mode()

    def game_rules(self):
        print("These are the rules: \n"
              "Rock crushes Scissors\n"
              "Scissors cuts Paper\n"
              "Paper covers Rock\n"
              "Rock crushes Lizard\n"
              "Lizard poisons Spock\n"
              "Spock smashes Scissors\n"
              "Scissors decapitates Lizard\n"
              "Lizard eats Paper\n"
              "Paper disproves Spock\n"
              "Spock vaporizes Rock\n")

    def choose_game_mode(self):
        user_input = input("Select 1 to play against a human, or 2 to play against the Npc.")
        if int(user_input) == 1:
            self.player_two = Human()
            self.player_two.name = input("What is player two's name?")
            print(f" {self.player_one.name} VS {self.player_two.name}")
            print()
            self.start_game()
            return self.player_two.name
        elif int(user_input) == 2:
            self.player_two = Npc()
            self.player_two.name = "Npc"
            print(f"You selected to play against Zora.")
            print("The game will now start!")
            print()
            self.start_game()
            return self.player_two.name
        elif int(user_input) > 2:
            print("Not Vaild Input. Try again.")
            self.choose_game_mode()

    def start_game(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            print(f"{self.player_one.name} will go first.")
            self.game_round()
        self.display_winner()

    def game_round(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.player_one.choose_your_gesture()
            print(f"{self.player_one.name} used {self.player_one.choose_gesture}.")
            print("")
            self.player_two.choose_your_gesture()
            print(f"{self.player_two.name} used {self.player_two.choose_gesture}.")
            if self.player_one.choose_gesture == self.player_two.choose_gesture:
                print("Same Gesture was chosen. It is a Tie.")
                print()
            elif self.player_one.choose_gesture == "Rock":
                if self.player_two.choose_gesture == "Scissors":
                    print(f"Rock crushes Scissor. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Lizard":
                    print(f"Rock crushes Lizard. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Spock":
                    print(f"Spock vaporizes Rock. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Paper":
                    print(f"Paper covers Rock. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
            elif self.player_one.choose_gesture == "Paper":
                if self.player_two.choose_gesture == "Rock":
                    print(f"Paper covers Rock. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Spock":
                    print(f"Paper disproves Spock. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()

                elif self.player_two.choose_gesture == "Scissors":
                    print(f"Scissors cuts Paper. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Lizard":
                    print(f"Lizard eats Paper. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
            elif self.player_one.choose_gesture == "Scissors":
                if self.player_two.choose_gesture == "Paper":
                    print(f"Scissors cuts Paper. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Lizard":
                    print(f"Scissors decapitates Lizard. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Rock":
                    print(f"Rock crushes Scissors. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Spock":
                    print(f"Spock smashes Scissors. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
            elif self.player_one.choose_gesture == "Lizard":
                if self.player_two.choose_gesture == "Spock":
                    print(f"Lizard poisons Spock. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Paper":
                    print(f"Lizard eats Paper. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Rock":
                    print(f"Rock crushes Lizard. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Scissors":
                    print(f"Scissors decapitates Lizard. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
            elif self.player_one.choose_gesture == "Spock":
                if self.player_two.choose_gesture == "Scissors":
                    print(f"Spock smashes Scissors. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Rock":
                    print(f"Spock vaporizes Rock. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Lizard":
                    print(f"Lizard poisons Spock. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()
                elif self.player_two.choose_gesture == "Paper":
                    print(f"Paper covers Rock. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(
                        f"{self.player_one.score} - {self.player_one.name}      {self.player_two.score} - {self.player_two.name}")
                    print()

    def display_winner(self):
        if self.player_one.score == 3:
            print(f"{self.player_one.name} wins")
        elif self.player_two.score == 3:
            print(f"{self.player_two.name} wins")
