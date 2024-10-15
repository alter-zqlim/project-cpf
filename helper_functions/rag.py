import streamlit as st
import numpy as np
from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

def loader(filepath):
  loader = PyPDFLoader(filepath)
  return loader.load()
