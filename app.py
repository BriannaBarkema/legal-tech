import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
from st_login_form import login_form
import requests
import os

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
            st.experimental_rerun()

def verify_address_with_usps(address, call_counter=0):
    # This URL and parameters will need to be updated according to the specific USPS API documentation.
    usps_api_url = "https://secure.shippingapis.com/ShippingAPI.dll"
    params = {
        "API": "Verify",
        "XML": f"<AddressValidateRequest USERID='your_usps_userid'><Address><Address1>{address['address1']}</Address1><Address2>{address['address2']}</Address2><City>{address['city']}</City><State>{address['state']}</State><Zip5>{address['zip']}</Zip5><Zip4/></Address></AddressValidateRequest>"
    }
    response = requests.get(usps_api_url, params=params)
    # You'll need to parse the XML response from USPS to determine if the address is valid.
    # This is a placeholder for the logic to parse the response and determine validity.
    is_valid = True  # This should be set based on the actual response
    standardized_address = {}  # This should be populated with the standardized address if valid
    return is_valid, standardized_address

def main_page():
    # Sidebar navigation but only for the Main Page
    st.sidebar.title("Main Navigation")
    page_options = ["Home", "Option 1", "Option 2"]  # Example options
    selected_option = st.sidebar.radio("Choose an option", page_options)

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
    with st.form("rent_details_form"):
        address_1 = st.text_input("Address 1")
        address_2 = st.text_input("Address 2")
        city = st.text_input("City")
        state = st.text_input("State")
        zip_code = st.number_input("ZIP Code")

        current_rent = st.number_input("Current Rent", format='%d')

        lo_name = st.text_input("Leasing Officer Name")
        lo_email = st.text_input("Leasing Officer Email")

        super_name = st.text_input("Supervisor Name")
        super_email = st.text_input("Supervisor Email")

        submitted = st.form_submit_button("Submit")  
        if submitted:
            address = {
                "address1": address_1,
                "address2": address_2,
                "city": city,
                "state": state,
                "zip": zip_code
            }
            # Assuming verify_address_with_usps is a function you have defined elsewhere
            # and it returns a boolean indicating validity and a dictionary with the standardized address
            is_valid, standardized_address = verify_address_with_usps(address)
            if is_valid:
                # Update the rent_details dictionary with all gathered information
                st.session_state["rent_details_complete"] = True
                st.session_state["rent_details"] = {
                    "address_1": address_1,
                    "address_2": address_2,
                    "city": city,
                    "state": state,
                    "zip_code": zip_code,
                    "current_rent": current_rent,
                    "lo_name": lo_name,
                    "lo_email": lo_email,
                    "super_name": super_name,
                    "super_email": super_email
                }
                st.success("Rent details submitted successfully.")
                st.experimental_rerun()
            else:
                st.error("The address could not be verified. Please check and try again.")

def app():
    # Determine the current page based on the completion status of previous pages
    if not st.session_state.get("authenticated", False):
        current_page = "Login"
    elif not st.session_state.get("basic_onboarding_complete", False):
        current_page = "Basic Onboarding"
    elif not st.session_state.get("rent_details_complete", False):
        current_page = "Rent Details"
    else:
        current_page = "Main Page"

    # Navigation pages dictionary
    pages = {
        "Login": login,
        "Basic Onboarding": onboarding_page,
        "Rent Details": rent_details_page,
        "Main Page": main_page
    }

    # Execute the current page function
    pages[current_page]()

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

if "rent_details_complete" not in st.session_state:
    st.session_state["rent_details_complete"] = False

app()
