from Enemy import *

class Zombie(Enemy):
    def __init__(self, health, attack):
        super().__init__(type_enemy = "Zombie", health = health, attack = attack)
    
    def talk(self):
        print(f"Grraaahh....!")
    
    def bite(self):
        print("The zombie bites you, causing damage!")