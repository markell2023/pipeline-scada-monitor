"""
Pipeline SCADA Monitor
Author: Markell Mitchell

Main application entry point.
"""

import time
from sensors.sensor_simulator import SensorSimulator
from alarms.alarm_manager import AlarmManager
from database.database_manager import DatabaseManager


def main():
    simulator = SensorSimulator()
    alarm_manager = AlarmManager()
    database_manager = DatabaseManager()


    print("===================================")
    print(" Pipeline SCADA Monitor")
    print(" Real-Time Sensor Feed")
    print("===================================")

    for reading_number in range(1, 11):
        reading = simulator.generate_reading()
        alarms = alarm_manager.check_alarms(reading)
        database_manager.save_reading(reading)

        print(f"\nReading #{reading_number}")
        print(f"Timestamp:   {reading['timestamp']}")
        print(f"Pressure:    {reading['pressure']} PSI")
        print(f"Temperature: {reading['temperature']} °F")
        print(f"Flow Rate:   {reading['flow_rate']} BBL/hr")

        if alarms:
            print("\n🚨 ACTIVE ALARMS:")
            for alarm in alarms:
                print(f"- {alarm}")
        else:
            print("\nSystem Status: NORMAL")

        time.sleep(1)


if __name__ == "__main__":
    main()