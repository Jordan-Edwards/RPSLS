class Player:
    def __init__(self):
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "Spock"]


    def show_gestures(self):
        print(f'{self.name}: Pick your Gesture!{self.gestures}')
        for single_gesture in self.gestures:
            print(single_gesture)

    def choose_gesture(self):
        print("Override this method")

