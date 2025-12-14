class Enemy:
    
    def __init__(self, type: str = "Goblin", health: int = 150, damage: int = 20):
        self.type = type
        self.health = health
        self.damage = damage


    def talk(self):
        print(f"I am a {self.type}. Be prepred to fight!")

    def walk(self):
        print(f"{self.type} moves closer !")
    
    def attack(self):
        print(f"{self.type} makes first move and attacked !")