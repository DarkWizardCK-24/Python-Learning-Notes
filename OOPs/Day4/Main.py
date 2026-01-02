from Zombie import *
from Vampire import *

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(100, 15)
vampire = Vampire(120, 20)

battle(zombie)
battle(vampire)