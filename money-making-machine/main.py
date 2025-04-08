import streamlit as st
import random
import time
import requests

st.title("Money Making Machine💵")

def generate_money():
    return random.randint(1, 1000) # This module is used to generate specific given amount of integers

st.subheader("Instant Cash Generator")

if st.button("Generate Money🤑"):
   st.write("Counting Your Money..")
   time.sleep(1)
   amount= generate_money()
   st.success(f"You Made ${amount}!")
