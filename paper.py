from gestures import Gestures


class Paper(Gestures):
    def __init__(self):
        super(Paper, self).__init__()
        self.name = "paper"
        self.wins_against = ["spock", "rock"]
        self.loses_against =["scissors", "lizard"]
