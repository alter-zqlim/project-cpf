import streamlit as st
import pandas as pd
from helper_functions import utility
from helper_functions import llm
from helper_functions import rag

# project page <title>
st.set_page_config(
    page_title = "Guide to Government Procurement",
    page_icon = ":material/shopping_cart:"
)

# page description
st.title(":blue[Guide to Government Procurement]")
st.markdown(
    """This app covers topics related to:  
    (i) General Information on Government Procurement for Suppliers;  
    (ii) Government Supplier Registration (GSR); as well as  
    (iii) Grounds for Debarment or Disqualification of Suppliers."""
)
st.divider()
st.write(
    "*Are you a budding business looking to transact with the government? Do you have further questions about government procurement? Ask away!*"
)

# password checkpoint
if not utility.check_password():  
    st.stop()

# specify sources
list_pdf = ["./data/Supplier_Guide_Detailed.pdf", "./data/AUTHORITY_AND_RATIONALE_FOR_DEBARMENT.pdf", "./data/Appln_Guidelines_for_Gov_Supp_Reg.pdf"]

# sample queries
st.markdown(
    """:blue[*Here are some sample queries (copy and paste to the submission box below) for you to get started*:  
    :material/adjust: What are some principles of government procurement?  
    :material/adjust: How do I register as a supplier?  
    :material/adjust: What if I default in performing the contract?]"""
)

data_reference = []  # init list to store loaded docs
for item in list_pdf:
    pdf_pages = utility.loader(item)  # loads PDF
    data_reference.extend(pdf_pages)

# splitted_documents = rag.text_splitter(data_reference)  # chunks loaded docs (PDF)
splitted_documents = rag.text_semantic_splitter(data_reference)  # semantic chunking of loaded docs (PDF)
db = rag.write_vector_store(splitted_documents)  # returns vector store of chunked docs
# st.write(db._collection.count())

# generate a form for user input
form = st.form(key = "form")
form.subheader("What would you like to know about government procurement?")

user_input = form.text_area(
    "Please enter your query below and press Submit", 
    height = 160
)

# on detecting Submit, processes and writes response to user input
if form.form_submit_button("Submit"):
    st.toast(f"User Input: {user_input}")
    response = rag.get_procurement_answer(user_input, db.as_retriever(search_type = "similarity_score_threshold", search_kwargs = {"score_threshold": 0.05}))
    if(response["context"] == []):
        st.write("I do not have the answer to that. Please rephrase your query or try a different one.")
    else:
        # st.write(response)  # full answer including input, context
        st.write(response["answer"])  # answer only
    
