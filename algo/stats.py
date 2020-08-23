import time


class Stats:
    def __init__(self):
        self.health = 500  # Base Hp
        self.strength_multiplier = 1  # No Multiplier
        self.strength = 100  # Base damage per hit
        self.corruption = 100  # sleep = 60 it takes 30 mins to go to corruption 5
        self.corruption_mutliplier = 0.90  # base multiplier
        self.luck = 0
        self.coins = 0  # currency obtained by opening chests

    def corrupt(self):
        position = 0
        while True:
            print(self.corruption)
            self.corruption = self.corruption * self.corruption_mutliplier
            time.sleep(0.5)

            if self.corruption <= 50 and position == 0:
                print(
                    "You're strength is deteriorating... You feel a sense of emptyness\n")
                self.strength_multiplier -= 0.20
                position += 1

            elif self.corruption <= 25 and position == 1:
                print(
                    "You're lack of will for life is near to none. You feel the entity creep into your mind\n")
                self.strength_multiplier -= 0.35
                position += 1

            elif self.corruption < 5:
                break

    def strength_stat(self, level):  # The level of power up. Level 1 Level 2 etc
        if level == 2:
            self.strength_multiplier += 0.25
        if level == 3:
            self.strength_multiplier += 0.20

        return self.strength * self.strength_multiplier


s1 = Stats()
s1.corrupt()
print(s1.strength_stat(1))
