# Pipeline SCADA Monitor

A Python-based SCADA monitoring and alarm management system that simulates industrial pipeline sensor data, stores readings in SQLite, detects alarm conditions, and displays operational metrics in a Streamlit dashboard.

## Features

- Real-time pipeline sensor simulation
- Pressure, temperature, and flow-rate monitoring
- Alarm detection for abnormal readings
- SQLite database storage
- Alarm history tracking
- Streamlit web dashboard
- Dark mode UI
- Trend charts and KPI metrics
- CSV alarm report export
- Git/GitHub version control

## Technologies Used

- Python
- SQLite
- SQL
- Streamlit
- Pandas
- Altair
- Git
- GitHub

## Project Structure

```text
pipeline-scada-monitor/
├── alarms/
│   └── alarm_manager.py
├── dashboard/
│   ├── dashboard_manager.py
│   └── streamlit_dashboard.py
├── database/
│   └── database_manager.py
├── sensors/
│   └── sensor_simulator.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
