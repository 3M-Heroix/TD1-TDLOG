from math import *
from Weapon import Weapon, Lance_missiles_antiair, Lance_missiles_antisurface, Lance_torpilles


class Vessel():
    def __init__(self, coordinates=tuple, max_hits=int, weapon=Weapon()):
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(x, y, z):
        print("GO TO (",x, y, z,')')

    def get_coordinates():
        pass

    # def get_coordinates():
    # pass

    # def fire_at():
    # pass


class Cruiser(Vessel):
    weapon = Lance_missiles_antiair()
    Rayon = weapon.rayon_action
    max_hits = 6

    def fire_at(self, x, y, z):
        assert self.__class__.max_hits != 0, "DestroyedError"
        T = self.coordinates
        self.distance = sqrt((T[0] - x) ** (2) + (T[1] - y) ** (2) + (T[2] - z) ** (2))
        assert self.distance < Cruiser.Rayon, "OutOfRangeError"
        Weapon.fire_at(x, y, z)  # il faut ne pas dépasser le nombre des ammunitions limite de l'arme en question

    def go_to(x, y, z):
        assert z == 0, "DisplacementNotPossible"
        return super().go_to(x, y, z)


class Submarine(Vessel):
    weapon = Lance_torpilles()
    Rayon = weapon.rayon_action
    max_hits = 2

    def fire_at(self, x, y, z):
        assert self.__class__.max_hits != 0, "DestroyedError"
        T = self.coordinates
        self.distance = sqrt((T[0] - x) ** (2) + (T[1] - y) ** (2) + (T[2] - z) ** (2))
        assert self.distance < Submarine.Rayon, "OutOfRangeError"
        Weapon.fire_at(x, y, z)  # il faut ne pas dépasser le nombre des ammunitions limite de l'arme en question

    def go_to(x, y, z):
        assert z in (-1, 0), "DisplacementNotPossible"
        return super().go_to(x, y, z)


class Fregate(Vessel):
    weapon = Lance_missiles_antisurface()
    Rayon = weapon.rayon_action
    max_hits = 5

    def fire_at(self, x, y, z):
        assert self.__class__.max_hits != 0, "DestroyedError"
        T = self.coordinates
        self.distance = sqrt((T[0] - x) ** (2) + (T[1] - y) ** (2) + (T[2] - z) ** (2))
        assert self.distance < Fregate.Rayon, "OutOfRangeError"
        Weapon.fire_at(x, y, z)  # il faut ne pas dépasser le nombre des ammunitions limite de l'arme en question

    def go_to(x, y, z):
        assert z == 0, "DisplacementNotPossible"
        return super().go_to(x, y, z)


class Destroyer(Vessel):
    weapon = Lance_torpilles()
    Rayon = weapon.rayon_action
    max_hits = 4

    def fire_at(self, x, y, z):
        assert self.__class__.max_hits != 0, "DestroyedError"
        T = self.coordinates
        self.distance = sqrt((T[0] - x) ** (2) + (T[1] - y) ** (2) + (T[2] - z) ** (2))
        assert self.distance < git Lance_torpilles.Rayon, "OutOfRangeError"
        Weapon.fire_at(x, y, z)  # il faut ne pas dépasser le nombre des ammunitions limite de l'arme en question

    def go_to(x, y, z):
        assert z == 0, "DisplacementNotPossible"
        return super().go_to(x, y, z)


class Aircraft(Vessel):
    weapon = Lance_missiles_antisurface()
    Rayon = weapon.rayon_action
    max_hits = 1

    def fire_at(self, x, y, z):
        assert self.__class__.max_hits != 0, "DestroyedError"
        T = self.coordinates
        self.distance = sqrt((T[0] - x) ** (2) + (T[1] - y) ** (2) + (T[2] - z) ** (2))
        assert self.distance < Aircraft.Rayon, "OutOfRangeError"
        Weapon.fire_at(x, y, z)  # il faut ne pas dépasser le nombre des ammunitions limite de l'arme en question

    def go_to(x, y, z):
        assert z == 1, "DisplacementNotPossible"
        return super().go_to(x, y, z)


