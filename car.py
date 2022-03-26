from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date, engine):
        self.last_service_date = last_service_date
        self.engine = engine

    def needs_service(self):
        return self.engine.engine_should_be_serviced()
