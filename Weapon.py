class Weapon :
    def __init__(self, ammunitions=int, range=int):
        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self, x=int, y=int, z=int) :
        self.x = x
        self.y = y
        self.z = z
        print("ATTACK ON (",x,y,z,')')


class Lance_missiles_antisurface(Weapon) :
    rayon_action = 30
    nbr_ammunitions = 40

    def fire_at(self, x, y, z):
        assert Lance_missiles_antisurface.nbr_ammunitions >0, "NoAmmunitionError"
        assert z==0, "OutOfRangeError"
        Lance_missiles_antisurface.nbr_munitions-=1
        return super().fire_at(x, y, z)     

class Lance_missiles_antiair(Weapon) :
    rayon_action = 40
    nbr_ammunitions = 15

    def fire_at(self, x, y, z):
        assert Lance_missiles_antiair.nbr_ammunitions >0, "NoAmmunitionError"
        assert z>0,"OutOfRangeError"
        Lance_missiles_antiair.nbr_ammunitions-=1
        return super().fire_at(x, y, z)

class Lance_torpilles(Weapon) :
    rayon_action = 20
    nbr_ammunitions = 15

    def fire_at(self, x, y, z):
        assert Lance_torpilles.nbr_ammunitions >0, "NoAmmunitionError"
        assert z<=0, "OutOfRangeError"
        Lance_torpilles.nbr_ammunitions-=1
        return super().fire_at(x, y, z)
        





#PO = Lance_missiles_antisurface(3, 4)
#print(PO.fire_at(1,1,1)==assertRaises("OutOfRangeError"))
#print(PO.range)
#return '{}: {} - {}'.format(premier_à_ecrie, deuxième_à_ecrire, 3_eme)
#on peut aussi écrire :
#return f"{premier}: {deuxième} - {troixième}
