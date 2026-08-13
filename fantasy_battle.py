import random


class Character:

    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed

    def take_damage(self, amount):
        dmg = max(1, amount - self.defense)
        self.health -= dmg

        if self.health < 0:
            self.health = 0

        return dmg

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        pass


class Warrior(Character):

    def __init__(self, name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage = 0

    def attack(self, target):

        damage = self.attack_power

        if self.health < 0.30 * self.max_health:
            damage = damage * 2
            print("💢", self.name, "(Warrior) enters Berserk Mode!")
            print("⚔", self.name, "strikes with double power!")

        else:
            print("⚔", self.name, "(Warrior) swings a sword!")

        actual_damage = target.take_damage(damage)

        print("Deals", actual_damage, "damage.")

        self.rage += 10


class Mage(Character):

    def __init__(self, name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed)
        self.mana = 100

    def attack(self, target):

        mana_cost = 30

        if self.mana >= mana_cost:

            damage = self.attack_power * 1.5

            self.mana -= mana_cost

            actual_damage = target.take_damage(damage)

            self.health -= 5

            if self.health < 0:
                self.health = 0

            print("🔥", self.name, "(Mage) casts Fireball!")
            print("Deals", actual_damage, "damage but loses 5 health.")

        else:

            damage = self.attack_power

            actual_damage = target.take_damage(damage)

            print("🔥", self.name, "(Mage) attacks normally!")
            print("Deals", actual_damage, "damage.")


class Archer(Character):

    def __init__(self, name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed)
        self.critical_chance = 0.30

    def attack(self, target):

        damage = self.attack_power

        if random.random() < self.critical_chance:

            damage = damage * 2

            actual_damage = target.take_damage(damage)

            print("🎯", self.name, "(Archer) lands a Critical Hit!")
            print("Deals", actual_damage, "damage.")

        else:

            actual_damage = target.take_damage(damage)

            print("🏹", self.name, "(Archer) shoots an arrow!")
            print("Deals", actual_damage, "damage.")


thor = Warrior("Thor", 130, 22, 12, 6)

gandalf = Mage("Gandalf", 90, 30, 5, 8)

alex = Archer("Alex", 100, 24, 7, 12)


fighters = [thor, gandalf, alex]


while len([fighter for fighter in fighters if fighter.is_alive()]) > 1:

    alive_fighters = []

    for fighter in fighters:
        if fighter.is_alive():
            alive_fighters.append(fighter)

    alive_fighters.sort(key=lambda fighter: fighter.speed, reverse=True)

    print()
    print("========== NEW ROUND ==========")

    for fighter in alive_fighters:

        if not fighter.is_alive():
            continue

        alive_targets = []

        for target in fighters:
            if target != fighter and target.is_alive():
                alive_targets.append(target)

        if len(alive_targets) == 0:
            break

        target = random.choice(alive_targets)

        print()
        print(fighter.name, "has", fighter.health, "HP.")

        fighter.attack(target)

        print(target.name, "has", target.health, "HP left.")

        if not target.is_alive():
            print("💀", target.name, "is defeated!")

        remaining = []

        for character in fighters:
            if character.is_alive():
                remaining.append(character)

        if len(remaining) == 1:
            break


winner = None

for fighter in fighters:
    if fighter.is_alive():
        winner = fighter


print()
print("================================")
print("🎉", winner.name, "wins the battle!")
print("================================")