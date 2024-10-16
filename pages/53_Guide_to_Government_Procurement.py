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

data_reference = rag.loader(debarment_guide)  # loads PDF
splitted_documents = rag.text_splitter(data_reference)  # chunks loaded doc (PDF)
db = rag.write_vector_store(splitted_documents)  # returns vector store of chunked doc
st.write(db._collection.count())

st.write(rag.get_procurement_answer("Who hosted the first Youth Olympics?", db.as_retriever()))
