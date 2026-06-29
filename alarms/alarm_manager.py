class AlarmManager:
    def check_alarms(self, reading):
        alarms = []

        if reading["pressure"] > 900:
            alarms.append("HIGH PRESSURE")

        if reading["temperature"] > 100:
            alarms.append("HIGH TEMPERATURE")

        if reading["flow_rate"] < 1150:
            alarms.append("LOW FLOW RATE")

        return alarms