import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000) # This module is used to generate specific given amount of integers

st.subheader("Instant Cash Generator")

if st.button("Generate Money🤑"):
   st.write("Counting Your Money..")
   time.sleep(1)
   amount= generate_money()
   st.success(f"You Made ${amount}!")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing")
   
    except:
        return ("Something Went Wrong")  

st.subheader("Side Hustle Ideas")       
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.warning(idea)

def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quotes"]
        else:
            return("Sometimes saying no to money is more powerful")
    except:
        return("Something Went Wrong!")
    
st.subheader("Motivational Quotes")
if st.button("Work Hard"):
    quote = fetch_money_quotes()
    st.info(quote)