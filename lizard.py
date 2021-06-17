from gestures import Gestures


class Lizard(Gestures):
    def __init__(self):
        super(Lizard, self).__init__()
        self.name = "lizard"
        self.wins_against = ["spock", "paper"]
        self.loses_against =["rock", "scissors"]
