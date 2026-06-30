import sqlite3


class DashboardManager:

    def __init__(self):
        self.database = "scada_monitor.db"

    def get_statistics(self):

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM sensor_readings")
        total_readings = cursor.fetchone()[0]

        cursor.execute("SELECT MAX(pressure) FROM sensor_readings")
        highest_pressure = cursor.fetchone()[0]

        cursor.execute("SELECT MIN(pressure) FROM sensor_readings")
        lowest_pressure = cursor.fetchone()[0]

        cursor.execute("SELECT AVG(temperature) FROM sensor_readings")
        average_temperature = cursor.fetchone()[0]

        cursor.execute("SELECT AVG(flow_rate) FROM sensor_readings")
        average_flow = cursor.fetchone()[0]

        connection.close()

        return {
            "total": total_readings,
            "max_pressure": highest_pressure,
            "min_pressure": lowest_pressure,
            "avg_temp": average_temperature,
            "avg_flow": average_flow
        }

    def get_recent_alarms(self):

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT timestamp, pressure, temperature, flow_rate, alarm_message
            FROM alarms
            ORDER BY id DESC
            LIMIT 10
        """)

        alarms = cursor.fetchall()

        connection.close()

        return alarms