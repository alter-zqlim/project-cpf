import streamlit as st
from langchain_community.document_loaders import PyPDFLoader

def loader(filepath):
  loader = PyPDFLoader(filepath)
  return loader.load()
