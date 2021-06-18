from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_your_gesture(self):
        print("Choose a gesture:")
        print("0 for Rock")
        print("1 for Paper")
        print("2 for Scissors")
        print("3 for Lizard")
        print("4 for Spock")
        human_selection = input()
        if int(human_selection) == 0:
            self.choose_gesture = self.gestures[0]
            return self.choose_gesture
        elif int(human_selection) == 1:
            self.choose_gesture = self.gestures[1]
            return self.choose_gesture
        elif int(human_selection) == 2:
            self.choose_gesture = self.gestures[2]
            return self.choose_gesture
        elif int(human_selection) == 3:
            self.choose_gesture = self.gestures[3]
            return self.choose_gesture
        elif int(human_selection) == 4:
            self.choose_gesture = self.gestures[4]
            return self.choose_gesture
        print()