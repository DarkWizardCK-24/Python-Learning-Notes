class Enemy:
    def __init__(self, type_enemy, health, attack_damage):
        self.type_enemy = type_enemy
        self.health = health
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.type_enemy}!")    
    
    def attack(self):   # <-- THIS MUST EXIST
        print(f"The {self.type_enemy} attacks for {self.attack_damage} damage!")