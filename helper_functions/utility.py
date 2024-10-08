import streamlit as st  
import random  
import hmac  

# """  
# This file contains the common components used in the Streamlit App.  
# This includes the sidebar, the title, the footer, and the password check.  
# """  

# function: check password input against Streamlit Secrets 
def check_password():  
    # returns True if user entered correct password  
    def password_entered():  
        # checks whether password entered by the user is correct  
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):  
            st.session_state["password_correct"] = True  
            del st.session_state["password"]  # do not store the password  
        else:  
            st.session_state["password_correct"] = False  
    # returns True if the passward is validated  
    if st.session_state.get("password_correct", False):  
        return True  
    # show input for password  
    st.text_input(  
        "Password",
        type = "password",
        on_change = password_entered,
        key="password"  
    )  
    if "password_correct" in st.session_state:  
        st.error("Password incorrect")  
    return False
