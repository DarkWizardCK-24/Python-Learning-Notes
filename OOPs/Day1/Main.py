from Day1.Enemy import Enemy

enemy = Enemy()

print(f"{enemy.type} has {enemy.health} health and does {enemy.damage} damage.")

print(enemy.talk())
print(enemy.walk())
print(enemy.attack())