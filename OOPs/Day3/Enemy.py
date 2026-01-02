class Enemy:
    def __init__(self, type_enemy, health, attack):
        self.type_enemy = type_enemy
        self.health = health
        self.attack = attack

    def talk(self):
        print(f"I am a {self.type_enemy}!")    