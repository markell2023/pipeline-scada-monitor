import random
from datetime import datetime


class SensorSimulator:
    def __init__(self):
        self.pressure = 850
        self.temperature = 95
        self.flow_rate = 1200

    def generate_reading(self):
        self.pressure += random.randint(-20, 25)
        self.temperature += random.randint(-4, 6)
        self.flow_rate += random.randint(-60, 45)

        self.pressure = max(780, min(self.pressure, 950))
        self.temperature = max(85, min(self.temperature, 108))
        self.flow_rate = max(1050, min(self.flow_rate, 1320))

        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pressure": self.pressure,
            "temperature": self.temperature,
            "flow_rate": self.flow_rate,
        }