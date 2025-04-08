import streamlit as st
import requests  # used to fetch data from api

st.markdown("""
    <style>
            
    .stApp h1 {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #044d3a;  /* optional: darker emerald shade */
    }
    .stApp {
        background-color: #a8f0c6; /* Light emerald green */
    }
    .joke-box {
        padding: 20px;
        background-color: #e6fff3;
        border: 2px solid #000000; /* Black border */
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        transition: all 0.5s ease-in-out;
        font-size: 18px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)


st.title("Random Joke Generator")

def get_random_joke():# fetching a random joke from inside of an api
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. pLease try again later."
    except:
        return "Why do programmers prefer dark mode? \n because light attracts bugs! " 
     
def main():
   
    st.write("Ready for a giggle😅? Click below!")

    if st.button("Get a Laugh🤣"):
        st.snow()
        with st.spinner("Loading Your Joke"): 
              joke = get_random_joke()


          # called the function inside joke variable which is fetching a joke#
        st.markdown(f"<div class='joke-box'>{joke}</div>", unsafe_allow_html=True)

        st.divider()
       
        st.markdown(
           """
<div style='text-align:center;'>
<p>Joke From Official Joke API</p>
<p>Built by Lubna</p>
""",
unsafe_allow_html= True
       )
        
        
if __name__ == "__main__":
    main()        
    
