class Weapon :
    def __init__(self, ammunitions, range):
        self.ammunitions = int(ammunitions)
        self.range = int(range)

    def fire_at(self, x, y, z) :
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        pass


class Lance_missiles_antisurface(Weapon) :
    rayon_action = 30
    nbr_munitions = 40

    def fire_at(self, x, y, z):
        assert Lance_missiles_antisurface.nbr_munitions >0, "NoAmmunitionError"
        assert z==0, "OutOfRangeError"
        return super().fire_at(x, y, z)

class Lance_missiles_antiair(Weapon) :
    rayon_action = 40
    nbr_munitions = 15

    def fire_at(self, x, y, z):
        assert Lance_missiles_antiair.nbr_munitions >0, "NoAmmunitionError"
        assert self.z>0,"OutOfRangeError"
        return super().fire_at(x, y, z)

class Lance_torpilles(Weapon) :
    rayon_action = 20
    nbr_munitions = 15

    def fire_at(self, x, y, z):
        assert Lance_torpilles.nbr_munitions >0, "NoAmmunitionError"
        assert self.z<=0, "OutOfRangeError"
        Lance_torpilles.nbr_munitions-=1
        return super().fire_at(x, y, z)

#PO = Lance_missiles_antisurface(3, 4)
#print(PO.fire_at(1,1,1)==assertRaises("OutOfRangeError"))
#print(PO.range)

