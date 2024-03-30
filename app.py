import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
from st_login_form import login_form

# Placeholder function for the chat GPT iframe
def chat_gpt():
    iframe_src = "https://chat.openai.com/g/g-S2mpeGXVc-r-ease-assistant"
    components.iframe(iframe_src, height=600, scrolling=True)

# Placeholder function for onboarding
def onboarding_page():
    st.title("Basic Onboarding")
    st.text("Let's get you started!")
    with st.form("onboarding_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email Address")
        dob = st.date_input("Date of Birth")

        # User can upload the lease document here
        lease_document = st.file_uploader("Upload Lease Document", type=['pdf'])

        submitted = st.form_submit_button("Submit")
        if submitted:
            if lease_document is not None:
                # Process or store the lease document as needed
                # For demonstration, we're just saving that the document has been uploaded
                lease_uploaded = True
            else:
                lease_uploaded = False
            st.session_state["basic_onboarding_complete"] = True
            st.session_state["user_info"] = {"first_name": first_name, "last_name": last_name, "dob": dob, "email": email, "lease_uploaded": lease_uploaded}
            st.success("Now let's get you to tell us more about your lease situation.")

# Main page content
def main_page():
    st.title("Welcome to the App")
    if st.session_state.get("username"):
        st.header(f"Hello, {st.session_state['username']}!")
    else:
        st.header("Welcome guest!")

    if st.session_state.get("user_info"):
        st.json(st.session_state["user_info"])
    
    st.header("Chat!")
    chat_gpt()

def rent_details_page():
    st.title("Rent Details")


# Sidebar navigation
def app():
    st.sidebar.title("Navigation")
    pages = {
        "Login": login,
        "Basic Onboarding": onboarding_page,
        "Rent Details": rent_details_page,
        "Main Page": main_page
    }

    if st.session_state.get("authenticated", False):
        page_selection = st.sidebar.radio("Go to", ["Basic Onboarding", "Rent Details", "Main Page"])
    else:
        page_selection = "Login"
    
    # Page navigation
    if page_selection == "Login":
        login()
    else:
        pages[page_selection]()

# Login function
def login():
    st.title("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Submit")
        if submitted:
            # Assuming login_form returns True for simplicity
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Logged in successfully")
            st.experimental_rerun()

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "basic_onboarding_complete" not in st.session_state:
    st.session_state["basic_onboarding_complete"] = False

app()
