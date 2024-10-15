import streamlit as st
import numpy as np
from helper_functions import llm

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma

from openai import OpenAI
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings

# all your (Open AI) password are belong to us
KEY_OPENAI = st.secrets["KEY_OPENAI_API"]
client = OpenAI(api_key = KEY_OPENAI)

def loader(filepath):
    loader = PyPDFLoader(filepath)
    return loader.load()

def text_splitter(pages):
    text_chunking = RecursiveCharacterTextSplitter(
        separators = ["\n\n", "\n", " ", ""],
        chunk_size = 500,
        chunk_overlap = 50,
        length_function = llm.count_tokens
    )
    return text_chunking.split_documents(pages)

def write_vector_store(splitted_documents):
    # Load the document, split it into chunks, embed each chunk and load it into the vector store.
    return Chroma.from_documents(
        splitted_documents,
        OpenAIEmbeddings(model = 'text-embedding-3-small'),
        persist_directory = "./chroma_db"
    )
