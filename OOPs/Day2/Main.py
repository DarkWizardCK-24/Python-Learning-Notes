from Enemy import * 

enemy = Enemy("Goblin", 150, 20)

print(f"{enemy.type} has {enemy.health} health and does {enemy.damage} damage.")

print(enemy.talk())
print(enemy.walk())
print(enemy.attack())