import Attacks as a

monsters = {
    # species: (max_hp, move1, move2, status_effect)
    "slime": ('Slime', 10, a.tackle, a.gooSpray, None),
    "hotpocket": ('Sentient Hot Pocket', 20, a.fireStarter, a.flamingSausage, None),
    "tank": ('Tank Test Dummy', 1000, a.wait, a.wait, None),
    "glass": ('Glassy Dummy', 1, a.wait, a.wait, None),
    "stem student": ('STEM Student', 69, a.trauma, a.digitsPi, None),
    "asian mom": ('Asian Mom', 80, a.woodenSpoon, a.comparison, None),
}


class Monster:
    def __init__(self, name):
        self.name = monsters[name][0]
        self.max_hp, self.current_hp = monsters[name][1], monsters[name][1]
        self.move1, self.move2 = monsters[name][2], monsters[name][3]
        self.status = monsters[name][4]
        self.exp, self.total_exp = 0, 0
        self.level = 1
        self.wins, self.losses = 0, 0

    def win_fight(self):
        self.current_hp = self.max_hp
        self.exp, self.total_exp = self.exp + 5, self.total_exp + 5
        self.wins += 1
        print(f'{self.name} wins! \n\tTotal wins: {self.wins}\n\tEXP gained: +5\n\t')

    def lose_fight(self):
        """resets hp and adds a loss to the counter"""
        self.current_hp = self.max_hp
        self.losses += 1

    def update_exp(self):
        """initializes the exp needed to level up your mon, then depending on what level you're at (1-9, 10-19, 20-29,
        etc.), it provides a multiplier to how much exp is needed.
        EX: Lv. 1-9 is 10 exp (base)
        Lv. 10-19 is 15 exp (*1.5)
        Lv. 20-29 is 30 exp (*2)
        Lv. 30-39 is 45 exp (*1.5) etc."""
        level_up_exp = 10
        if (self.level // 10) % 2 == 0 and self.level // 10 > 0:
            level_up_exp *= 1.5
        elif (self.level // 10) % 2 != 0 and self.level // 10 > 0:
            level_up_exp *= 2

        """logs how many times a monster would level up with its current exp, tells the user, and levels them up those
        many times. Every 5 levels, damaging moves gain +1 dmg, and every level health gets raised by 1."""
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
        """Prints the relevant stats about your monster object. Currently unused outside of testing."""
        print('#' * 50)
        print(f'Monster: {self.name}, HP: {self.current_hp}/{self.max_hp}')
        print(f'Level: {self.level}, EXP to level up: {self.exp}, Total EXP: {self.total_exp}')
        print(f'Moves:\n{self.move1}\n{self.move2}')
        print(f'Total Wins: {self.wins}')
        print(f'Total Losses: {self.losses}')
        print('#' * 50)

    def attack_menu(self):
        """A condensed version of .print_stats() used when battling."""
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
        while atk.lower().capitalize() != self.move1.name and atk.lower().capitalize() != self.move2.name:
            atk = input(f"That is not a valid attack. Here are all valid attacks for this monster: "
                        f"{self.move1.name}, {self.move2.name}\n")

        def _atk_output(move):
            """Created to minimize repetitive code, executes various text messages based on the attack used."""
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

        # Checks if an attack input matches either move 1 or move 2 for that mon, then executes the move if it does.
        if atk.lower().capitalize() == self.move1.name:
            _atk_output(self.move1)
        elif atk.lower().capitalize() == self.move2.name:
            _atk_output(self.move2)
