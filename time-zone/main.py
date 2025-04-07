# libraries to be imported
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of given time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Asia/Dubai",
    "Europe/Berlin",
]

# title of the app
st.title("Time Zone App")

# helps create a multi select dropdown for time zones given in the list above
selected_timezone = st.multiselect("Select Timezone", TIME_ZONES, default=["UTC", "Asia/Karachi"])

# shows the time zones that is being select from the drop down
st.subheader("Selected Timezones")
for tz in selected_timezone:

    # it helps in getting the correct time for each zone in AM or PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())
from_tz = st.selectbox('From Timezone', TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.success(f"{to_tz}: {converted_time}")
