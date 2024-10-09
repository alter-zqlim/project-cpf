import streamlit as st
import numpy as np
import os
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken
from helper_functions.utility import check_password
from helper_functions import llm

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# generate embedding
def get_embedding(input, model = 'text-embedding-3-small'):
    response = client.embeddings.create(
        input = input,
        model = model
    )
    return [x.embedding for x in response.data]

# helper function for calling LLM
def get_completion(prompt, model = "gpt-4o-mini", temperature = 0, top_p = 1.0, max_tokens = 1024, n = 1, json_output = False):
    # used to force output as json if specified
    if json_output == True:
      output_json_structure = {"type": "json_object"}
    else:
      output_json_structure = None

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(  # originally was openai.chat.completions
        model = model,
        messages = messages,
        temperature = temperature,
        top_p = top_p,
        max_tokens = max_tokens,
        n = 1,
        response_format = output_json_structure,
    )
    return response.choices[0].message.content

# helper function that takes in "messages" as the parameter (as opposed to prompt)
def get_completion_by_messages(messages, model = "gpt-4o-mini", temperature = 0, top_p = 1.0, max_tokens = 1024, n = 1):
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature,
        top_p = top_p,
        max_tokens = max_tokens,
        n = 1
    )
    return response.choices[0].message.content

# functions for counting tokens
def count_tokens(text):
    encoding = tiktoken.encoding_for_model('gpt-4o-mini')
    return len(encoding.encode(text))

def count_tokens_from_message(messages):
    encoding = tiktoken.encoding_for_model('gpt-4o-mini')
    value = ' '.join([x.get('content') for x in messages])
    return len(encoding.encode(value))


# all your passwords are belong to us (Open AI)
KEY_OPENAI = st.secrets['KEY_OPENAI_API']
client = OpenAI(api_key = KEY_OPENAI)

os.environ["OPENAI_API_VERSION"] = "2024-03-01-preview"
os.environ["OPENAI_API_KEY"] = KEY_OPENAI
embeddings_model = OpenAIEmbeddings(model='text-embedding-3-small')

loader = PyPDFLoader("https://www.developer.tech.gov.sg/products/collections/data-science-and-artificial-intelligence/playbooks/prompt-engineering-playbook-beta-v3.pdf")
pages = loader.load()

st.write(pages[0])

# Let's count how many token are there
# by summing all the token counts from every page
# Don't worry about understand the code in this cell
list_of_tokencounts = []
for page in pages:
    list_of_tokencounts.append(count_tokens(page.page_content))

st.write(f"There are total of {np.sum(list_of_tokencounts)} tokens")

text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=500,
    chunk_overlap=50,
    length_function=count_tokens
)

splitted_documents = text_splitter.split_documents(pages)

st.write(len(splitted_documents))
st.write(splitted_documents[17])
"""
db = Chroma.from_documents(
    splitted_documents,
    embeddings_model,
    persist_directory="./chroma_db"
)
st.write(db._collection.count())
"""

loader_web = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader_web.load()
splitted_data = text_splitter.split_documents(data)

# vectordb = Chroma.from_documents(documents=splitted_data, embedding=embeddings_model)
