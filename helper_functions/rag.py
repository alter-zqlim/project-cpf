import streamlit as st
import numpy as np
from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

from helper_functions import llm

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
