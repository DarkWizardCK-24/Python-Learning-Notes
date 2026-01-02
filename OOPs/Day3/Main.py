from Zombie import *
from Vampire import *

zombie = Zombie(health=100, attack=15)
vampire = Vampire(health=120, attack=20)

print(f"{zombie.type_enemy} - Health: {zombie.health}, Attack: {zombie.attack}")
print(f"{vampire.type_enemy} - Health: {vampire.health}, Attack: {vampire.attack}")
print(vampire.talk())
print(vampire.drink_blood())
print(zombie.talk())
print(zombie.bite())