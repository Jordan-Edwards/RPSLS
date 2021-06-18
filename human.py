from player import Player

class Human(Player):
    def choosing_gesture(self):
        self.choosing_gesture = int(input("Enter a choice (rock 0, paper 1, scissors 2, Lizard 3, Spock 5): "))
        self.chosen_gesture = self.gestures_list