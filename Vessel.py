from Weapon import Weapon, Lance_missiles_antiair, Lance_missiles_antisurface, Lance_torpilles

class Vessel(Weapon) :
    def __init__(self, weapon = Weapon(), maxhits = int, coordinates=tuple) :
        self.weapon = weapon
        self.coordinates = coordinates

    def se_deplace(self, x, y, z):
        

class Cruiser(Vessel) :
    weapon = Lance_missiles_antiair()
    
    def

    def go_to(x, y, z):


    





weapon = Weapon(3,2)
print(weapon.range)

abissa = Vessel(weapon, (0,0))
print(abissa.weapon)