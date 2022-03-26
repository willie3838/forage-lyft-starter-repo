from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        return sum(self.wear) >= 3