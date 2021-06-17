from gestures import Gestures


class Spock(Gestures):
    def __init__(self):
        super(Spock, self).__init__()
        self.name = "spock"
        self.wins_against = ["scissors", "rock"]
        self.loses_against =["paper", "lizard"]
