from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
        self.value = "human"

    def show_gestures(self):
        print(f'{self.name}: These are your choices{self.gestures}')
        for single_gesture in self.gestures:
            print(single_gesture)

    def choose_gesture(self):
        pass
