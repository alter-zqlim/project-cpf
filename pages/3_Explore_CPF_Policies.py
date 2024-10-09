import streamlit as st
from helper_functions.utility import check_password
from helper_functions import llm
from langchain_community.document_loaders import PyPDFLoader

from langchain_openai import ChatOpenAI
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
llmodel = ChatOpenAI(model = "gpt-4o-mini")

st.set_page_config(
    page_title = "Explore CPF Policies",
    page_icon=":material/group:"
)

st.title("Explore CPF Policies")
st.write(
    "Users can explore different CPF policies through interactive scenarios that illustrate how various policies apply to real-life situations (e.g., housing withdrawals, healthcare financing). This feature will enhance understanding by allowing users to see the practical implications of CPF policies in their lives."
)

# password checkpoint
if not check_password():  
    st.stop()

form = st.form(key = "form")
form.subheader("What would you like to know about CPF policies?")

user_prompt = form.text_area(
    "Please enter your query below", 
    height = 160
)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = llm.get_completion(user_prompt)
    st.write(response)
    print(f"User Input is {user_prompt}")


file_path = "./data/food-waste-minimisation-guidebook-for-food-manufacturing-establishments.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
st.write(len(docs))
st.write(docs[0].page_content[0:100])
st.write(docs[0].metadata)

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
splits = text_splitter.split_documents(docs)
vectorstore = InMemoryVectorStore.from_documents(
    documents = splits, embedding = OpenAIEmbeddings(model='text-embedding-3-small')
)

retriever = vectorstore.as_retriever()
