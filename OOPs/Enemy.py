class Enemy:
    type : str = "Goblin"
    health : int = 100
    damage : int = 10

    def talk(self):
        print(f"I am a {Enemy.type}. Be prepred to fight!")

    def walk(self):
        print(f"{Enemy.type} moves closer !")
    
    def attack(self):
        print(f"{Enemy.type} makes first move and attacked !")