import sqlite3
import streamlit as st
import pandas as pd
import time


DATABASE = "scada_monitor.db"


def load_sensor_data():
    connection = sqlite3.connect(DATABASE)
    query = "SELECT * FROM sensor_readings ORDER BY id DESC"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


def load_alarm_data():
    connection = sqlite3.connect(DATABASE)
    query = "SELECT * FROM alarms ORDER BY id DESC"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


st.set_page_config(page_title="Pipeline SCADA Monitor", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: #FAFAFA;
}

[data-testid="stSidebar"] {
    background-color: #161B22;
}

h1, h2, h3 {
    color: #58A6FF;
}

[data-testid="stMetricValue"] {
    color: #FAFAFA;
}

[data-testid="stMetricLabel"] {
    color: #C9D1D9;
}

div[data-testid="stDataFrame"] {
    background-color: #161B22;
}

.alarm-card {
    background-color: #3B0D0D;
    padding: 18px;
    border-radius: 10px;
    border-left: 6px solid #FF4B4B;
    color: #FFFFFF;
    font-weight: bold;
}

.normal-card {
    background-color: #0F3D2E;
    padding: 18px;
    border-radius: 10px;
    border-left: 6px solid #2ECC71;
    color: #FFFFFF;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Dashboard Controls")

auto_refresh = st.sidebar.checkbox("Auto-refresh", value=False)
refresh_seconds = st.sidebar.slider("Refresh every seconds", 2, 10, 5)

if auto_refresh:
    time.sleep(refresh_seconds)
    st.rerun()

st.title("Pipeline SCADA Monitor")
st.subheader("SCADA Sensor Dashboard")

sensor_data = load_sensor_data()
alarm_data = load_alarm_data()

if sensor_data.empty:
    st.warning("No sensor readings found.")
else:
    total_alarms = len(alarm_data)

    if total_alarms > 0:
        st.markdown(
            '<div class="alarm-card">🚨 System Status: ACTIVE ALARMS DETECTED</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="normal-card">✅ System Status: NORMAL</div>',
            unsafe_allow_html=True
        )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Readings", len(sensor_data))
    col2.metric("Highest Pressure", f"{sensor_data['pressure'].max()} PSI")
    col3.metric("Average Temperature", f"{sensor_data['temperature'].mean():.1f} °F")
    col4.metric("Average Flow Rate", f"{sensor_data['flow_rate'].mean():.1f} BBL/hr")
    col5.metric("Total Alarms", total_alarms)

    st.divider()

    st.subheader("🚨 Alarm Center")

    if alarm_data.empty:
        st.success("No alarms recorded.")
    else:
        st.dataframe(alarm_data.head(10), width="stretch")

        st.download_button(
            label="📥 Download Alarm Report",
            data=alarm_data.to_csv(index=False),
            file_name="alarm_report.csv",
            mime="text/csv"
        )

        alarm_counts = alarm_data["alarm_message"].value_counts()
        st.bar_chart(alarm_counts)

    st.divider()

    st.subheader("Recent Sensor Readings")
    st.dataframe(sensor_data.head(10), width="stretch")

    st.subheader("Pressure Trend")
    st.line_chart(sensor_data.sort_values("id")[["id", "pressure"]].set_index("id"))

    st.subheader("Temperature Trend")
    st.line_chart(sensor_data.sort_values("id")[["id", "temperature"]].set_index("id"))

    st.subheader("Flow Rate Trend")
    st.line_chart(sensor_data.sort_values("id")[["id", "flow_rate"]].set_index("id"))