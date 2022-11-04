#from re import X


class Weapon :
    def __init__(self, ammunitions=int, range=int):
        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = z
        print('ATTACK')


class Lance_missiles_antisurface(Weapon) :
    rayon_action = 30
    nbr_munitions = 40

    def fire_at(self, x, y, z):
        assert Lance_missiles_antisurface.nbr_munitions >0, "NoAmmunitionError"
        assert z==0, "OutOfRangeError"
        Lance_missiles_antisurface.nbr_munitions-=1
        return super().fire_at(x, y, z)     

class Lance_missiles_antiair(Weapon) :
    rayon_action = 40
    nbr_munitions = 15

    def fire_at(self, x, y, z):
        assert Lance_missiles_antiair.nbr_munitions >0, "NoAmmunitionError"
        assert z>0,"OutOfRangeError"
        Lance_missiles_antiair.nbr_munitions-=1
        return super().fire_at(x, y, z)

class Lance_torpilles(Weapon) :
    rayon_action = 20
    nbr_munitions = 15

    def fire_at(self, x, y, z):
        assert Lance_torpilles.nbr_munitions >0, "NoAmmunitionError"
        assert z<=0, "OutOfRangeError"
        Lance_torpilles.nbr_munitions-=1
        return super().fire_at(x, y, z)
        






#return '{}: {} - {}'.format(premier_à_ecrie, deuxième_à_ecrire, 3_eme)
#on peut aussi écrire :
#return f"{premier}: {deuxième} - {troixième}
