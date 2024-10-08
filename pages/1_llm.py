import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken
from helper_functions.utility import check_password
from helper_functions import llm

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("https://www.developer.tech.gov.sg/products/collections/data-science-and-artificial-intelligence/playbooks/prompt-engineering-playbook-beta-v3.pdf")
pages = loader.load()

st.write(pages[0])
