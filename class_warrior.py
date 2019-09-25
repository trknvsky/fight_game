from random import randint


class Warrior:
    def __init__(self, warrior_1, warrior_2, warrior_3):
        self.warrior_1 = warrior_1
        self.warrior_2 = warrior_2
        self.warrior_3 = warrior_3

    warrior_1 = {
        'name': 'strength man',
        'power': 15,
        'skill': randint(1, 3),
        'health': 100
    }

    warrior_2 = {
         'name': 'agility man',
         'power': 10,
         'skill': randint(1, 3),
         'health': 100
     }

    warrior_3 = {
         'name': 'intelligence man',
         'power': 12,
         'skill': randint(1, 3),
         'health': 100
    }

