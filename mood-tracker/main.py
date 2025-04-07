import streamlit as st # For creating web interface
import pandas as pd # For data manipulation
import datetime # For handling dates
import csv # For reading and writing CSV file
import os # For file operations

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    
    if not os.path.exists(MOOD_FILE):
       
        return pd.DataFrame(columns=["Date", "Mood"])
    
    return pd.read_csv(MOOD_FILE)


def save_mood_data(date, mood):
  
    with open(MOOD_FILE, "a") as file:

       
        writer = csv.writer(file)

        writer.writerow([date, mood])
        

# CSS for bg colour
st.markdown("""
    <style>
    .stApp {
        background: #e8d9c1;
    }
    </style>
""", unsafe_allow_html=True)


st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Anxious", "Sleepy", "Nervous"])


if st.button("Log Mood"):
    
    
    save_mood_data(today, mood)

    
    st.success("Mood Logged Successfully!")

data = load_mood_data()

if not data.empty:

    st.subheader("Mood History")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

    # CSS for name tag
    st.markdown('<div style="border:2px solid #5C4033;border-radius:10px;padding:10px;text-align:center;color:#5C4033;background:#fef9f5;font-weight:bold;">Built by Lubna Noor</div>', unsafe_allow_html=True)

   
    