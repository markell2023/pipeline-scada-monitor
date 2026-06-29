import sqlite3


class DatabaseManager:
    def __init__(self, database_name="scada_monitor.db"):
        self.database_name = database_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.database_name)

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

    def save_reading(self, reading):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO sensor_readings (timestamp, pressure, temperature, flow_rate)
            VALUES (?, ?, ?, ?)
        """, (
            reading["timestamp"],
            reading["pressure"],
            reading["temperature"],
            reading["flow_rate"]
        ))

        connection.commit()
        connection.close()