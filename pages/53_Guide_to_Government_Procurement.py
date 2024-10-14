import streamlit as st
import pandas as pd
from helper_functions import utility
from helper_functions import llm

# project page <title>
st.set_page_config(
    page_title = "Guide to Government Procurement",
    page_icon=":material/shopping_cart:"
)

# page description
st.title("Guide to Government Procurement")
st.write(
    "Are you a budding business looking to transact with the government? Do you have questions about government procurement? Ask away!"
)

# password checkpoint
if not utility.check_password():  
    st.stop()
