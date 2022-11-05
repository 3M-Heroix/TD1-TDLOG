import unittest
from Weapon import Weapon, Lance_missiles_antiair, Lance_missiles_antisurface, \
    Lance_torpilles  # cette line est facultative parcequ'il est écrite dans fichier VESSEL.py
from math import *
from vaisseaux import Cruiser, Submarine, Fregate, Destroyer, Aircraft


class Test_Cruiser(unittest.TestCase):
    # L = Lance_missiles_antisurface(4, 1)
    def test_fire_at(self):
        weapon = Lance_missiles_antiair(1, 1, 1)
        L = Cruiser((1, 1, 1), max_hits=6, weapon=weapon)
        L.fire_at(100, 100, 1).assertRaises(OutOfRangeError)  # Failed ok

    def test_go_to(self):
        weapon = Lance_missiles_antiair(1, 1, 1)
        L = Cruiser((1, 1, 1), max_hits=6, weapon=weapon)
        L.go_to(1, 1, 1).assertRaises("DisplacementNotPossible")


class Test_Submarine(unittest.TestCase):
    # L = Lance_missiles_antisurface(4, 1)
    def test_fire_at(self):
        weapon = Lance_torpilles(1, 1, -1)
        L = Submarine((1, 1, 1), max_hits=2, weapon=weapon)
        L.fire_at(100, 100, 1).assertRaises(OutOfRangeError)  # Failed ok

    def test_go_to(self):
        weapon = Lance_torpilles(1, 1, -1)
        L = Submarine((1, 1, 1), max_hits=2, weapon=weapon)
        L.go_to(1, 1, 1).assertRaises("DisplacementNotPossible")  # z in (-1, 0)


class Test_Fregate(unittest.TestCase):
    # L = Lance_missiles_antisurface(4, 1)
    def test_fire_at(self):
        weapon = Lance_missiles_antisurface(1, 1, 0)
        L = Fregate((1, 1, 1), max_hits=5, weapon=weapon)
        L.fire_at(100, 100, 0).assertRaises(OutOfRangeError)  # Failed ok

    def test_go_to(self):
        weapon = Lance_missiles_antisurface(1, 1, 0)
        L = Fregate((1, 1, 1), max_hits=5, weapon=weapon)
        L.go_to(1, 1, 1).assertRaises("DisplacementNotPossible")  # Failed ok Z==0


class Test_Destroyer(unittest.TestCase):
    # L = Lance_missiles_antisurface(4, 1)
    def test_fire_at(self):
        weapon = Lance_torpilles(1, 1, -1)
        L = Destroyer((1, 1, 1), max_hits=4, weapon=weapon)
        L.fire_at(100, 100, 0).assertRaises(OutOfRangeError)  # Failed ok

    def test_go_to(self):
        weapon = Lance_torpilles(1, 1, -1)
        L = Destroyer((1, 1, 1), max_hits=4, weapon=weapon)
        L.go_to(1, 1, 1).assertRaises("DisplacementNotPossible")  # Failed ok z==0


class Test_Aircraft(unittest.TestCase):
    # L = Lance_missiles_antisurface(4, 1)
    def test_fire_at(self):
        weapon = Lance_missiles_antisurface(1, 1, 0)
        L = Aircraft((1, 1, 1), max_hits=1, weapon=weapon)
        L.fire_at(100, 100, 0).assertRaises(OutOfRangeError)  # Failed ok

    def test_go_to(self):
        weapon = Lance_missiles_antisurface(1, 1, 0)
        L = Aircraft((1, 1, 1), max_hits=1, weapon=weapon)
        L.go_to(1, 1, 0).assertRaises("DisplacementNotPossible")  # il faut z==1 pour que le test passe


# Total des erreurs = 10

if __name__ == '__main__':
    unittest.main()