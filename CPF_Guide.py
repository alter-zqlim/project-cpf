import streamlit as st
import pandas as pd
import numpy as np
import langchain
from helper_functions.utility import check_password  


# for query
from langchain_chroma import Chroma
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

if not check_password():  
    st.stop()

# main page header
st.write("# Welcome to your friendly guide on understanding CPF policies")

# manifest sidebar
st.sidebar.success("Select a demo above.")


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




st.markdown(
    """
    Streamlit
    """
)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# load_data, puts in Pandas dataframe
# converts the date from text to datetime
# accepts parameter (nrows), i.e. num_rows to load into the dataframe
# cache it
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe.
data = load_data(10000)

# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

# create a checkbox to show raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# mapping all pickups
# st.subheader('Map of all pickups')
# st.map(data)

# mapping pickups at 1700
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
