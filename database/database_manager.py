import sqlite3


class DatabaseManager:

    def __init__(self):
        self.database = "scada_monitor.db"
        self.create_table()
        self.create_alarm_table()

    def connect(self):
        return sqlite3.connect(self.database)

    def create_table(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sensor_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                pressure INTEGER,
                temperature INTEGER,
                flow_rate INTEGER
            )
        """)

        connection.commit()
        connection.close()

    def create_alarm_table(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alarms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                pressure INTEGER,
                temperature INTEGER,
                flow_rate INTEGER,
                alarm_message TEXT
            )
        """)

        connection.commit()
        connection.close()

    def save_reading(self, reading):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO sensor_readings
            (timestamp, pressure, temperature, flow_rate)
            VALUES (?, ?, ?, ?)
        """, (
            reading["timestamp"],
            reading["pressure"],
            reading["temperature"],
            reading["flow_rate"]
        ))

        connection.commit()
        connection.close()

    def save_alarm(self, reading, alarm_message):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO alarms
            (timestamp, pressure, temperature, flow_rate, alarm_message)
            VALUES (?, ?, ?, ?, ?)
        """, (
            reading["timestamp"],
            reading["pressure"],
            reading["temperature"],
            reading["flow_rate"],
            alarm_message
        ))

        connection.commit()
        connection.close()