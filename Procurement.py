import streamlit as st
import pandas as pd
import numpy as np

# for query
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI


# project page <title>
st.set_page_config(
    page_title="CPF Policies Guide",
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

# main page header
st.write("# For businesses: How to go about providing goods and services to the government")
st.write("*Hello Entrepreneur! Congratulations on setting up your business and we hope you see ever increasing sales! Through this web application, you can learn more about transacting with the government to deliver goods and services!*")
st.write("*Please note that there are ***NO*** procurement opportunities on this web application. Head over to https://www.gebiz.gov.sg/ to search for those opportunities.*")
st.write(":material/west::material/west: Select an app on the left to get started.")

st.image("./assets/image.webp")
# manifest sidebar
# st.sidebar.success("Select an app above.")
