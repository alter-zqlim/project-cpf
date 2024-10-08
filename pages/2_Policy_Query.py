import streamlit as st
import pandas as pd
import numpy as np
import langchain
from helper_functions.utility import check_password  

# for query
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI


# project page <title>
st.set_page_config(
    page_title="CPF Policies Query",
    page_icon=":material/group:",
)

# mandatory disclaimer for project
EXPANDER_NOTICE = """
**IMPORTANT NOTICE**: This web application is a prototype developed for **educational purposes** only.
The information provided here is **NOT intended for real-world usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

**Furthermore, please be aware that the LLM may generate inaccurate or incorrect information.
You assume full responsibility for how you use any generated output.**

Always consult with qualified professionals for accurate and personalised advice.
"""

expander = st.expander(":red[Disclaimer]", True)
expander.write(EXPANDER_NOTICE)

st.markdown("# CPF Policy Explainer")
st.write(
    "*Please enter the password to continue.*"
)

# password checkpoint
if not check_password():  
    st.stop()

# user input area (form)
form = st.form(key = "form")
form.write(
    "Explore different CPF policies through interactive scenarios that illustrate how various policies apply to real-life situations (e.g., housing withdrawals, healthcare financing). Examine the practical implications of CPF policies on citizens."
)

user_prompt = form.text_area(
    "What CPF policies would you like to learn about?",
    height = 160
)

# Load blog post
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(data)

# VectorDB
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=splits, embedding=embedding)

"""
question = "What are the approaches to Task Decomposition?"
llm = ChatOpenAI(temperature=0)
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(), llm=llm
)
"""
