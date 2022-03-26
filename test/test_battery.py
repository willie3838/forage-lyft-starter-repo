import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def isServicable(self):
        last_service_date = datetime.today.year() + 3
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())
    
    def isNotServicable(self):
        last_service_date = datetime.today().year()
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())