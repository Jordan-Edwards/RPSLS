from gestures import Gestures


class Rock(Gestures):
    def __init__(self):
        super(Rock, self).__init__()
        self.name = "rock"
        self.wins_against = ["scissors", "lizard"]
        self.loses_against =["paper", "spock"]
