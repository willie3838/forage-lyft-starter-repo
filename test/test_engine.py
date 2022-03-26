import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def isServicable(self):
        current_mileage = 3001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
    
    def isNotServicable(self):
        current_mileage = 3003
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()