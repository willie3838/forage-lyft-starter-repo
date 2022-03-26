from pyexpat import model
from car import Car
import os, sys; sys.path.append(os.path.dirname(os.path.realpath("./engine/carFactory.py")))
from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
class CarFactory:

    def createCalliope(last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, CapuletEngine(current_mileage, last_service_mileage))

    def createGlissade(last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, WilloughbyEngine(current_mileage, last_service_mileage))
    
    def createPalindrome(last_service_date, warning_light_is_on):
        return Car(last_service_date, SternmanEngine(warning_light_is_on))
    
    def createRorschach(last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, WilloughbyEngine(current_mileage, last_service_mileage))
    
    def createThovex(last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, CapuletEngine(current_mileage, last_service_mileage))