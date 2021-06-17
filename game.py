


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = (pass)

    def run_game(self):
        # Intro
        # Display a welcome message
        print ('Welcome to my Python game!')




        # Instructions for play/rules




        # Choose game mode - Single player or Multi player
        def choose_game_mode(self):
            print("How many players?")
            response = input()
            if response == 2:
                self.player_two = Human()
            else:
                self.player_two = npc()

        # Game Rounds
        # Player one chooses gesture
        # Player two chooses gesture
        # Determine winner of round, winner's score increases
        # Loop to continue gameplay until best of three occurs

        # End Game
        # Display winner of game
        # Prompt to play again? - Not MVP
        pass
    def choose_game_mode(self):
        print("How many players?")
        response = input()
        if response == 2:
            self.player_two = Human()
        else:
            self.player_two = AI()



