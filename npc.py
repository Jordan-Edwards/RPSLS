from player import Player
import random
import time


class Npc(Player):
    def __init__(self):
        super().__init__()

    def choose_your_gesture(self):
        time.sleep(1)
        self.choose_gesture = random.choice(self.gestures)
