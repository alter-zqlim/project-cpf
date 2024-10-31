import streamlit as st
import pandas as pd
import csv

from helper_functions import utility
from helper_functions import llm
from helper_functions import rag

from langchain_core.documents import Document

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

from langchain_experimental.agents import create_csv_agent
from langchain.agents.agent_types import AgentType

# project page <title>
st.set_page_config(
    page_title = "Exploring Procurement Data",
    page_icon=":material/shopping_cart:"
)

# page description
st.title("Exploring Procurement Data")
st.image("./assets/history.jpg")
st.write(
    "Users can explore procurement data from GeBiz, based on various procuring agencies, from FY2019 to FY2023."
)

# st.cache_data.clear()

# specify sources
data_input_filepath = "./data/GovernmentProcurementviaGeBIZ.csv"

# determine embeddings and metadata
columns_to_embed = ["tender_description"]
columns_to_metadata = ["tender_no", "agency", "award_date", "tender_detail_status", "supplier_name", "awarded_amt"]

# split and write data to vector store
docs = []
max_tokens = 0
with open(data_input_filepath, newline = "", encoding = "utf-8-sig") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for i, row in enumerate(csv_reader):
        to_metadata = {col: row[col] for col in columns_to_metadata if col in row}
        values_to_embed = {k: row[k] for k in columns_to_embed if k in row}
        to_embed = "\n".join(f"{k.strip()}: {v.strip()}" for k, v in values_to_embed.items())
        newDoc = Document(page_content = to_embed, metadata = to_metadata)
        docs.append(newDoc)
        r = llm.count_tokens(str(newDoc))
        if(r > max_tokens):
            max_tokens = r
            
st.write(max_tokens)
# gebiz_documents = rag.char_splitter(docs)
# db = rag.write_vector_store(gebiz_documents)  # returns vector store of split docs
# st.write(db._collection.count())

# password checkpoint
if not utility.check_password():  
    st.stop()

pandas_agent = llm.init_pandas_dataframe_agent(df)
csv_agent = llm.init_csv_agent("./data/GovernmentProcurementviaGeBIZ.csv")

agencies_default_list = [
    "Competition and Consumer Commission of Singapore (CCCS)"
]

agencies_default_list_alt = [
    "Agency for Science, Technology and Research",
    "Competition and Consumer Commission of Singapore (CCCS)",
    "Economic Development Board",
    "Energy Market Authority of Singapore",
    "Enterprise Singapore",
    "Jurong Town Corporation",
    "Sentosa Development Corporation",
    "Singapore Tourism Board",
    "Ministry of Trade & Industry-Ministry Headquarter",
    "Ministry of Trade & Industry-Department of Statistics"
]

# read GeBiz data file, set index to "agency", sort by specified columns, construct index with unique values
unsorted_df = utility.get_GeBIZ_data(data_input_filepath, data_input_index)
df = unsorted_df.sort_values(by = [data_input_index, "tender_no", "supplier_name", "award_date"])

# generate a multi-option selector that displays data based on selected agencies  
agencies = st.multiselect(
    "Select agencies",
    list(df.agency.unique()),
    agencies_default_list
)

# generate a multi-option selector that displays data based on tender status  
tender_statuses = st.multiselect(
    "Filter information by tender award status for selected agencies",
    list(df.tender_detail_status.unique())[::-1],
    ["Award by interface record", "Awarded by Items", "Awarded to No Suppliers", "Awarded to Suppliers"]
)

if not agencies or not tender_statuses:
    st.error("Please select at least one agency AND one tender status.")
else:
    data = df[(df["agency"].isin(agencies)) & (df["tender_detail_status"].isin(tender_statuses))]
    st.write("## Procurement projects", data.sort_index())

# generate a form for user input
form = st.form(key = "form")
form.subheader("What would you like to know about the above set of historical GeBiz procurement data?")

user_input = form.text_area(
    "Please enter your query below and press Submit", 
    height = 120
)

# on detecting Submit, processes and writes response to user input
if form.form_submit_button("Submit"):
    st.toast(f"User Input: {user_input}")
    st.write(user_input)
