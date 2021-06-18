class Player:
    def __init__(self):
        self.name = input("What name would you like to go by?")
        self.score = 0
        self.gestures_list = ["rock", "paper", "scissors", "lizard", "spock"]
        self.gestures_list[0] = 1
        self.gestures_list[1] = 2
        self.gestures_list[2] = 3
        self.gestures_list[3] = 4
        self.gestures_list[4] = 5

    # def show_gestures(self):
    #    for single_gesture in self.gestures:
    #       print(single_gesture)

    # def choose_gesture(self):
    #   input([self.gestures])
    #   def choose_gesture(self, player_2,):
