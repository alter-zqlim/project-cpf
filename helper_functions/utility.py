import streamlit as st  
import pandas as pd
import random  
import hmac

from langchain_community.document_loaders import PyPDFLoader

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

# function: read csv, set index
@st.cache_data
def get_GeBIZ_data(filepath, index):
    df = pd.read_csv(filepath)
    return df.set_index(index, drop = False)

# function: read, load pdf
@st.cache_data
def loader_pdf(filepath):
    loader = PyPDFLoader(filepath)
    return loader.load()
