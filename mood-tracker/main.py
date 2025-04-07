import streamlit as st         # for creating web interface
import pandas as pd            # for manipulating data
import datetime                # for handling dates
import csv                     # for reading and writing CSV files
import os                      # for file operations

#Define the file name for storing data
MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)


def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:

        writer = csv.writer(file)
        writer.writerow([date , mood])

st.title("Mood Tracker")        

today = datetime.date.today()

st.subheader("How Are You Feeling Today?")
mood = st.selectbox("Select Your Mood", ["Happy", "Sad", "Joyful", "Anxious", "Angry", "Relaxed", "Motivated", "Frustrated", "Tired"])

if st.button("Log Mood"):
    save_mood_data(today, mood)

    st.success("Mood Logged Successfully")

data = load_mood_data()
if not data.empty:
    st.subheader("Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

# A little bit of css for tag💓
    st.markdown("""
<div style='display: inline-block; background-color: #ffe6f0; color: #800000; padding: 6px 12px; 
             border: 2px solid #8B0000; border-radius: 20px; font-weight: 600; font-size: 14px;
             box-shadow: 1px 1px 3px rgba(0,0,0,0.1);'>
    Built by Lubna Noor
</div>
""", unsafe_allow_html=True)
