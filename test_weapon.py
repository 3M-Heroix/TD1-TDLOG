import unittest
from Weapon import Weapon, Lance_missiles_antiair, Lance_missiles_antisurface, Lance_torpilles

class Test_Lance_missiles_antisurface(unittest.TestCase):
    #L = Lance_missiles_antisurface(4, 1)
    def test_fire_at(self):
        L = Lance_missiles_antisurface(4,1)
        L.fire_at(1,1,1).assertRaise(OutOfRangeError) #Failed ok

class Test_Lance_missiles_antiair(unittest.TestCase):

    def test_fire_at(self):
        L = Lance_missiles_antiair(4,1)
        L.fire_at(1,1,-1).assertRaise(OutOfRangeError)#Failed ok

class Test_Lance_torpilles(unittest.TestCase):

    def test_fire_at(self):
        L = Lance_torpilles(4,1)
        L.fire_at(1,1,1).assertRaise(OutOfRangeError)#Failed ok






if __name__ == '__main__' :
    unittest.main()
