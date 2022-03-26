import unittest
from tires.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def isServicable(self):
        wear = [0.9,0.1,0.1,0.1]
        tire = CarriganTire(wear)
        self.assertTrue(tire.needs_service())
    
    def isNotServicable(self):
        wear = [0.1,0.1,0.1,0.1]
        tire = CarriganTire(wear)
        self.assertFalse(tire.needs_service())
