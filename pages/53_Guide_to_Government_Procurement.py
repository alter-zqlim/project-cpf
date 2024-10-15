import streamlit as st
import pandas as pd
from helper_functions import utility
from helper_functions import llm
from helper_functions import rag

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

debarment_guide = "./data/AUTHORITY_AND_RATIONALE_FOR_DEBARMENT.pdf"
data_reference = rag.loader(debarment_guide)  # outputs 'pages'
splitted_documents = rag.text_splitter(data_reference)
st.write(len(splitted_documents))
st.write(data_reference[0].metadata)
