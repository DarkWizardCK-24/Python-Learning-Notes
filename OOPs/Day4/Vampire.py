from Enemy import *

class Vampire(Enemy):
    def __init__(self, health, attack_damage):
        super().__init__(type_enemy = "Vampire", health = health, attack_damage = attack_damage)
    
    def talk(self):
        print(f"I am a {self.type_enemy}!")

    def drink_blood(self):
        print("The vampire is drinking blood to satisfy its thirst!")