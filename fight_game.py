from class_warrior import Warrior
from random import randint


class Game(Warrior):
    def attributes(self, choose, player, opponent):
        self.player = player
        self.opponent = opponent
        self.choose = choose

    @staticmethod
    def fight():
        print('SUPER FIGHT GAME !!!\n')
        player = None
        opponent = None

        choose = int(input('Select a warrior: 1 - strong, 2 - agility, 3 - intelligence: '))
        if choose == 1:
            player = Warrior.warrior_1
        elif choose == 2:
            player = Warrior.warrior_2
        elif choose == 3:
            player = Warrior.warrior_3

        opponent_random = randint(1, 3)

        while opponent_random == choose:
            opponent_random = randint(1, 3)


        if opponent_random == 1:
            opponent = Warrior.warrior_1
        elif opponent_random == 2:
            opponent = Warrior.warrior_2
        elif opponent_random == 3:
            opponent = Warrior.warrior_3

        print('Your warrior: ', player['name'])
        print('Opponent\'s warrior', opponent['name'])

        win = False
        while True:
            print('Your player HP: ', player['health'])
            print('Opponent    HP: ', opponent['health'], '\n')

            kick = int(input('Please select kick: 1 - to head, 2 - to body, 3 - to foot : '))
            block = int(input('Please select block: 1 - to head, 2 - to body, 3 - to foot : '))
            print('\n')
            opponent_kick = randint(1, 3)
            opponent_block = randint(1, 3)

            if kick == opponent_block:
                print('Opponent blocked your kick')

            if kick != opponent_block:
                (opponent['health']) = opponent['health'] - (player['power'] * player['skill'])
                print('You hit an opponent', str(player['skill']) + 'x', 'damage')

            if block == opponent_kick:
                print('You blocked opponents kick')

            if block != opponent_kick:
                player['health'] = player['health'] - (opponent['power'] * opponent['skill'])
                print('Opponent hits you', str(opponent['skill']) + 'x damage')

            if player['health'] <= 0:
                break

            if opponent['health'] <= 0:
                win = True
                break

        if win:
            print('YOU WINNER!!!')
        else:
            print('GAME OVER.')


Game.fight()


