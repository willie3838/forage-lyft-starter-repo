from battery import Battery
from datetime import datetime


class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        if datetime.today().year() - self.last_service_date.year() >= 4:
            return True
        return False