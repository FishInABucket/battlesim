from Monsters import *


def battle(m1, m2):
    """simulates the actual attack between 2 monster objects, returning the winner upon a victory."""
    round_num = 0
    while True:
        round_num += 1
        print('ROUND', round_num)

        m1.fight(m2)
        if m2.current_hp <= 0:
            m1.win_fight()
            m2.lose_fight()
            m1.update_exp()
            return m1

        m2.fight(m1)
        if m1.current_hp <= 0:
            m2.win_fight()
            m1.lose_fight()
            m2.update_exp()
            return m2


def pick_monster(mon, num):
    """Checks if the input matches an existing monster ID, if it doesn't then it spits an error message and prompts
    the user to provide another response. If it matches, it creates a monster object with that same ID."""
    while mon not in monsters:
        mon = input(f'Pick your {num} monster: ')
        mon = mon.lower()
        if mon.lower() not in monsters:
            print('Please pick an existing monster.')
            print(f'List of current monsters:', end=' ')
            for i in range(len(monsters)):
                if tuple(monsters.keys())[i] is not tuple(monsters.keys())[-1]:
                    print(tuple(monsters.keys())[i], end=', ')
                else:
                    print(tuple(monsters.keys())[-1])
    return Monster(mon)


if __name__ == '__main__':
    print(f'-' * 20, 'Pick your monsters', '-' * 20)
    """Initialize monster variables"""
    p1 = ''
    p2 = ''

    """Monster Selection"""
    p1 = pick_monster(p1, 'first')
    p2 = pick_monster(p2, 'second')

    """battling"""
    print(f'-' * 20, 'BATTLE BEGIN', '-' * 20)
    p1 = battle(p1, p2)
    while True:
        ans = input('Would you like to continue battling with the winner?\n')
        while ans.lower() != 'yes' and ans.lower() != 'no' and ans.lower() != 'y' and ans.lower != 'n':
            print('Please respond with either "yes"/"y" or "no"/"n".')
            ans = input('Would you like to continue battling with the winner?\n')
        if ans.lower() == 'no' or ans.lower() == 'n':
            print('Alright, thank you for playing!')
            break
        elif ans.lower() == 'yes' or ans.lower() == 'y':
            p2 = pick_monster(p2, 'second')
            battle(p1, p2)

"""
------------------------CURRENT BUGS-----------------------------------------------------------------
* Status effects only applying their effects for one turn

------------------------TO BE IMPLEMENTED -----------------------------------------------------------
* implement super effective and not very effective attacks
* allow for saving of a monster to a csv file that can be loaded up later
* allow for saving of attacks to a csv file that can be referenced later

-----------------------------------------------------------------------------------------------------
"""
