from gestures import Gestures


class Scissors(Gestures):
    def __init__(self):
        super(Scissors, self).__init__()
        self.name = "scissors"
        self.wins_against = ["paper", "lizard"]
        self.loses_against =["spock", "rock"]

