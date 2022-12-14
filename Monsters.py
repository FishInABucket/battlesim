import Attacks as a

monsters = {
    # species: (max_hp, move1, move2, status_effect)
    "slime": (10, a.tackle, a.gooSpray, None),
    "hockypocky": (20, a.firestarter, a.infernoSausage, None),
    "test dummy": (1000, a.wait, a.wait, None)
}


class Monster:
    def __init__(self, name):
        self.name = name
        self.max_hp, self.current_hp = monsters[name][0], monsters[name][0]
        self.move1, self.move2 = monsters[name][1], monsters[name][2]
        self.status = monsters[name][3]
        self.exp, self.total_exp = 0, 0
        self.level = 1
        self.wins, self.losses = 0, 0

    def win_fight(self):
        self.current_hp = self.max_hp
        self.exp, self.total_exp = self.exp + 5, self.total_exp + 5
        self.wins += 1
        print(f'{self.name} wins! \n\tTotal wins: {self.wins}\n\tEXP gained: +5\n\t')

    def lose_fight(self):
        self.current_hp = self.max_hp
        self.losses += 1

    def update_exp(self):
        level_up_exp = 10
        if (self.level // 10) % 2 == 0 and self.level // 10 > 0:
            level_up_exp *= 1.5
        elif (self.level // 10) % 2 != 0 and self.level // 10 > 0:
            level_up_exp *= 2
        levelups = self.exp // level_up_exp
        if levelups > 0:
            print(f'LEVELED UP! {self.level} -> {self.level + levelups}\n\tHP: +1')
        for o in range(levelups):
            self.exp -= level_up_exp
            self.level += 1
            if self.level % 5 == 0:
                print('\tMove Damage: +1')
                if self.move1.dmg != 0:
                    self.move1.dmg += 1
                if self.move2.dmg != 0:
                    self.move2.dmg += 1
            self.max_hp += 1
            self.current_hp += 1
        print(f'EXP to level up: {level_up_exp - self.exp}')

    def print_stats(self):
        print('#' * 50)
        print(f'Monster: {self.name}, HP: {self.current_hp}/{self.max_hp}')
        print(f'Level: {self.level}, EXP to level up: {self.exp}, Total EXP: {self.total_exp}')
        print(f'Moves:\n{self.move1}\n{self.move2}')
        print(f'Total Wins: {self.wins}')
        print(f'Total Losses: {self.losses}')
        print('#' * 50)

    def attack_menu(self):
        print('#' * 50)
        print(f'{self.name}, HP: {self.current_hp}/{self.max_hp}')
        print(f'Moves:\n{self.move1}\n{self.move2}')
        print('#' * 50)

    def fight(self, other):
        """returns battle winner"""

        # checks for if either mon has no hp remaining
        if self.current_hp > 0 and other.current_hp <= 0:
            return self.name
        elif other.current_hp > 0 and self.current_hp <= 0:
            self.lose_fight()
            other.win_fight()
            return other.name
        elif (self.current_hp and other.current_hp) == 0:
            return None

        self.attack_menu()
        atk = input("Pick an attack: ")
        if atk == self.move2.name:
            print(True)
        while atk != self.move1.name and atk != self.move2.name:
            atk = input(f"That is not a valid attack. Here are all valid attacks for this monster: "
                        f"{self.move1.name}, {self.move2.name}")

        def _atk_output(move):
            if move.dmg > 0:
                other.current_hp -= move.dmg
                print(f'{self.name} hit {other.name} with {move.name} for {move.dmg} damage!')
                if move.effect is not None:
                    print(f'{move.name} inflicted {other.name} with {move.effect}!')
                    move.effect_activate(other)
            if move.dmg == 0 and move.effect is not None:
                print(f'{move.name} inflicted {other.name} with {move.effect}!')
            elif move.dmg <= 0 and move.effect is None:
                'Error 1: Something unexpected happened'
            else:
                'Error 2: something unexpected happened'

        if atk == self.move1.name:
            _atk_output(self.move1)
        elif atk == self.move2.name:
            _atk_output(self.move2)


if __name__ == '__main__':
    print(f'-' * 20, 'Pick your monsters', '-' * 20)
    """Initialize monster variables"""
    p1 = ''
    p2 = ''

    """
    Monster Selection
    """
    while p1 not in monsters:
        p1 = input('Pick your first monster: ')
        p1 = p1.lower()
        if p1.lower() not in monsters:
            print('Please pick an existing monster.')
            print(f'List of current monsters:', end=' ')
            for i in range(len(monsters)):
                if tuple(monsters.keys())[i] is not tuple(monsters.keys())[-1]:
                    print(tuple(monsters.keys())[i], end=', ')
                else:
                    print(tuple(monsters.keys())[-1])
    p1 = Monster(p1)

    while p2 not in monsters:
        p2 = input('Pick your second monster: ')
        p2 = p2.lower()
        if p2.lower() not in monsters:
            print('Please pick an existing monster.')
            print(f'List of current monsters:', end=' ')
            for i in range(len(monsters)):
                if tuple(monsters.keys())[i] is not tuple(monsters.keys())[-1]:
                    print(tuple(monsters.keys())[i], end=', ')
                else:
                    print(tuple(monsters.keys())[-1])
    p2 = Monster(p2)

    """
    battling
    """
    print(f'-' * 20, 'BATTLE BEGIN', '-' * 20)
    round_num = 1
    while True:
        if p1.fight(p2) == p1.name:
            p1.win_fight()
            p2.lose_fight()
            p1.update_exp()
            break
        round_num += 1
        if p2.fight(p1) == p2.name:
            p2.win_fight()
            p1.lose_fight()
            p2.update_exp()
            break
        round_num += 1

