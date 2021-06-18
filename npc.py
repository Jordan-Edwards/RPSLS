from player import Player
import random


class Npc(Player):
    def __init__(self):
        super().__init__(self)
        self.choice = random.randint(0, len(self.gestures))
        self.name = "Zora"
        self.value = 'Npc'
