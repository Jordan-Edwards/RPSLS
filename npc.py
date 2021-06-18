from player import Player
import random
n = 1


class Npc(Player):
    def chosen_gesture(self):
        self.chosen_gesture = random.choice(self.gestures_list)
        print(self.chosen_gesture)
