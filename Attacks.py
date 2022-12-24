import random


def chance_25(status):
    if random.randint(1, 4) == 1:
        return status
    else:
        return None


class Attacks:
    def __init__(self, name, type_, dmg, desc, effect=None):
        self.name = name.capitalize()
        self.type = type_
        self.dmg = dmg
        self.desc = desc
        self.effect = effect

    def __str__(self):
        return f"{self.name} \n\tMove Typing: {self.type} \n\tDamage: {self.dmg} \n\tDescription: {self.desc}\n"

        # FIXME: status effects not applying effects for longer than a single move
    def effect_activate(self, opp):
        if self.effect.lower() == 'paralysis':
            if random.randint(1, 4) == 1:
                return 'paralysis'
        elif self.effect.lower() == 'burn':
            opp.current_hp -= 1
            return 'burn'
        elif self.effect.lower() == 'poison':
            opp.current_hp -= opp.max_hp * 0.1
            return 'poison'
        elif self.effect.lower() == 'sleep':
            round_num = 0
            if round_num == 3:
                return False
            elif round_num == 2:
                if random.randint(1, 3) != 3:
                    return False
            elif round_num == 1:
                if random.randint(1, 4) != 4:
                    return False
            else:
                return 'sleep'


########################################################################################################################
tackle = Attacks('tackle', 'Normal', 3, "The user charges against the opponent, hitting them with the full force of "
                                        "their weight.")
gooSpray = Attacks('goo spray', 'Poison', 2, "The user spits a wad of goo on the opponent with a 25% chance to"
                                             " inflict poison on them.", chance_25('poison'))
flamingSausage = Attacks('Flaming Sausage', 'Fire', 8, "The hot pocket opens itself up, spilling its contents\n"
                                                       "on you. 25% chance to be burned.", chance_25('burn'))
fireStarter = Attacks('fire starter', 'Fire', 0, "The user lights the opponent on fire, causing burn status.", 'burn')

wait = Attacks('wait', 'Normal', 0, "The user does nothing, just sits and waits.")

trauma = Attacks('traumatize', 'Psychic', 5, 'The user trauma dumps all their pain upon the opponent, leaving them\n'
                                             'with psychological scarring and requiring therapy for the rest of their\n'
                                             'life.')
digitsPi = Attacks("1 million digits of pi", 'Psychic', 2, 'The user recites 1 million digits of pi at such a fast \n'
                                                           'rate that the opponent loses half their braincells.')

woodenSpoon = Attacks('Wooden Spoon', 'Fighting', 6, 'The user slams the opponent upside the head with a wooden spoon.')

comparison = Attacks('Comparing to your Cousin', 'Psychic', 3, 'The user compares the opponent to their cousin who \n'
                                                               'always seems to do everything right while they always\n'
                                                               'seem to do everything wrong.')

