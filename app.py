import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components

from st_login_form import login_form

def chat_gpt():
    iframe_src = "https://chat.openai.com/g/g-S2mpeGXVc-r-ease-assistant"
    components.iframe(iframe_src)


# Function to display the onboarding page
def onboarding_page():
    st.title("Onboarding")
    st.text("Let's get you started!")
    with st.form("onboarding_form"):
        # Example fields
        fullname = st.text_input("First Name")
        email = st.text_input("Email Address")
        age = st.number_input("Age", step=1, format="%d")
        bio = st.text_area("Bio")

        submitted = st.form_submit_button("Submit")
        if submitted:
            # Save the user's onboarding info, for example, in session state or a database
            st.session_state["onboarding_complete"] = True
            st.session_state["user_info"] = {"fullname": fullname, "email": email, "age": age, "bio": bio}
            st.success("Onboarding Complete! Welcome to the platform.")
            main_page()

# Function to display the main content after login and onboarding
def main_page():
    st.title("Welcome to the App")
    if st.session_state.get("username"):
        st.header(f"Hello, {st.session_state['username']}!")
    else:
        st.header("Welcome guest!")
    
    # Display user info as an example
    if st.session_state.get("user_info"):
        st.json(st.session_state["user_info"])

    st.header("Chat!")
    chat_gpt()

# Initialize login form
client = login_form()

if st.session_state.get("authenticated", False):
    if not st.session_state.get("onboarding_complete", False):
        # User is authenticated but has not completed onboarding
        onboarding_page()
    else:
        # User is authenticated and has completed onboarding
        main_page()
else:
    st.error("Not authenticated")
