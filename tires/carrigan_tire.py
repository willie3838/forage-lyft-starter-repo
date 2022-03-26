from tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear):
        self.wear = wear
        
    def needs_service(self):
        for num in self.wear:
            if num >= 0.9:
                return True
        return False