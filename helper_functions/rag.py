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

from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain import hub
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI

from langchain_experimental.text_splitter import SemanticChunker

__import__('pysqlite3')
import sys
import pysqlite3
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

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
        OpenAIEmbeddings(model = 'text-embedding-3-small', openai_api_key = st.secrets["KEY_OPENAI_API"]),
        persist_directory = "./chroma_db"
    )

def get_procurement_answer(user_query, vector_base):
    template = """You are an assistant for question-answering tasks. Only use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
    Context: {context}
    Answer:
    """
    retrieval_qa_chat_prompt = ChatPromptTemplate.from_messages(
        [("system", template), ("human", "{input}")]
    )
    # prompt = ChatPromptTemplate.from_template("Summarize this content: {context}")
    
    # retrieval_qa_chat_prompt = PromptTemplate.from_template(template)
    large_lang_model = ChatOpenAI(model = "gpt-3.5-turbo", openai_api_key = st.secrets["KEY_OPENAI_API"])

    combine_docs_chain = create_stuff_documents_chain(large_lang_model, retrieval_qa_chat_prompt)
    rag_chain = create_retrieval_chain(vector_base, combine_docs_chain)
    
    return rag_chain.invoke({"input": user_query})


