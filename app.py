import time

from sensors.sensor_simulator import SensorSimulator
from alarms.alarm_manager import AlarmManager
from database.database_manager import DatabaseManager
from dashboard.dashboard_manager import DashboardManager


def main():
    simulator = SensorSimulator()
    alarm_manager = AlarmManager()
    database_manager = DatabaseManager()
    dashboard_manager = DashboardManager()

    print("===================================")
    print("      Pipeline SCADA Monitor")
    print("      Real-Time Sensor Feed")
    print("===================================")

    for reading_number in range(1, 11):
        reading = simulator.generate_reading()
        alarms = alarm_manager.check_alarms(reading)

        database_manager.save_reading(reading)

        print(f"\nReading #{reading_number}")
        print(f"Timestamp:    {reading['timestamp']}")
        print(f"Pressure:     {reading['pressure']} PSI")
        print(f"Temperature:  {reading['temperature']} °F")
        print(f"Flow Rate:    {reading['flow_rate']} BBL/hr")

        if alarms:
            print("\n🚨 ACTIVE ALARMS:")
            for alarm in alarms:
                print(f"- {alarm}")
                database_manager.save_alarm(reading, alarm)
        else:
            print("\nSystem Status: NORMAL")

        time.sleep(1)

    stats = dashboard_manager.get_statistics()
    recent_alarms = dashboard_manager.get_recent_alarms()

    print("\n==============================")
    print("      SCADA DASHBOARD")
    print("==============================")
    print(f"Total Readings:      {stats['total']}")
    print(f"Highest Pressure:    {stats['max_pressure']} PSI")
    print(f"Lowest Pressure:     {stats['min_pressure']} PSI")
    print(f"Average Temperature: {stats['avg_temp']:.1f} °F")
    print(f"Average Flow Rate:   {stats['avg_flow']:.1f} BBL/hr")

    print("\n==============================")
    print("      ALARM CENTER")
    print("==============================")

    if recent_alarms:
        for alarm in recent_alarms:
            print(
                f"{alarm[0]} | {alarm[4]} | "
                f"Pressure: {alarm[1]} PSI | "
                f"Temp: {alarm[2]}°F | "
                f"Flow: {alarm[3]} BBL/hr"
            )
    else:
        print("No alarms recorded.")


if __name__ == "__main__":
    main()

    