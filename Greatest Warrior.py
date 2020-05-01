class Warrior:
    """
    Warrior class from the top solution to the kata
    """
    def __init__(self):
        self._experience = 100
        self.rs = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion",
                   "Master", "Greatest"]
        self.achievements = []

    def training(self, train):
        if train[2] > self.level:
            return "Not strong enough"
        self._experience += train[1]
        self.achievements.append(train[0])
        return train[0]

    def battle(self, lvl):
        diff = lvl - self.level
        if 0 >= lvl or lvl > 100:
            return "Invalid level"
        if diff >= 5 and (lvl // 10) > (self.level // 10):
            return "You've been defeated"
        if diff > 0:
            self._experience += 20 * diff * diff
            return "An intense fight"
        if diff > -2:
            self._experience += 5 if diff == -1 else 10
            return "A good fight"
        return "Easy fight"

    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.rs[self.experience // 1000]

    @property
    def experience(self):
        return min(10000, self._experience)


class Warrior:
    """
    My Warrior class
    """
    def __init__(self):
        self.ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.rank = self.ranks[0]
        self.level = 1
        self.experience = 100
        self.achievements = []

    def leveling(self, xp):
        self.experience += xp
        if self.experience > 10000:
            self.experience = 10000
        while int(self.experience / 100) > self.level:
            self.level += 1
        while self.ranks.index(self.rank) < int(self.level/10):
            self.rank = self.ranks[self.ranks.index(self.rank) + 1]

    def training(self, args):
        description, xp, min_level = args
        if self.level < min_level:
            return "Not strong enough"
        else:
            self.leveling(xp)
            self.achievements.append(description)
            return description

    def battle(self, enemy_level):
        if 1 > enemy_level or enemy_level > 100:
            return "Invalid level"
        enemy_rank = self.ranks[int(enemy_level/10)]
        if self.ranks.index(self.rank) < self.ranks.index(enemy_rank) and self.level <= enemy_level-5:
            return "You've been defeated"

        diff = enemy_level - self.level
        if diff <= -2:
            return "Easy fight"
        elif diff == -1:
            self.leveling(5)
            return "A good fight"
        elif not diff:
            self.leveling(10)
            return "A good fight"
        elif diff >= 1:
            self.leveling(20 * diff**2)
            return "An intense fight"
