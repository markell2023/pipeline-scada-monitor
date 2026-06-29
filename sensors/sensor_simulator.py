import random
from datetime import datetime


class SensorSimulator:
    def __init__(self):
        self.pressure = 850
        self.temperature = 95
        self.flow_rate = 1200

    def generate_reading(self):
        self.pressure += random.randint(-8, 8)
        self.temperature += random.randint(-2, 2)
        self.flow_rate += random.randint(-25, 25)

        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pressure": self.pressure,
            "temperature": self.temperature,
            "flow_rate": self.flow_rate,
        }