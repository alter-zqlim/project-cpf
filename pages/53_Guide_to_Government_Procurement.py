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

# specify source
debarment_guide = "./data/AUTHORITY_AND_RATIONALE_FOR_DEBARMENT.pdf"

data_reference = utility.loader(debarment_guide)  # loads PDF
splitted_documents = rag.text_splitter(data_reference)  # chunks loaded doc (PDF)
db = rag.write_vector_store(splitted_documents)  # returns vector store of chunked doc
st.write(db._collection.count())

# generate a form for user input
form = st.form(key = "form")
form.subheader("What would you like to know about authority and rationale for debarment?")

user_input = form.text_area(
    "Please enter your query below and press Submit", 
    height = 160
)

# on detecting Submit, processes and writes response to user input
if form.form_submit_button("Submit"):
    st.toast(f"User Input: {user_input}")
    response = rag.get_procurement_answer(user_input, db.as_retriever())
    st.write(response["answer"])
    
