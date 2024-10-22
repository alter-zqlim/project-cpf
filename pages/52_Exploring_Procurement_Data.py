import streamlit as st
import pandas as pd
from helper_functions import utility
from helper_functions import llm

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
st.write(
    "Users can explore procurement data from GeBiz, based on various procuring agencies, from FY2019 to FY2023."
)

# st.cache_data.clear()

# specify sources
data_input_filepath = "./data/GovernmentProcurementviaGeBIZ.csv"
data_input_index = "agency"

# read GeBiz data file, set index to "agency", sort by specified columns, construct index with unique values
unsorted_df = utility.get_GeBIZ_data(data_input_filepath, data_input_index)
df = unsorted_df.sort_values(by = ["tender_no", "supplier_name", "award_date"])
df_index = df[~df.index.duplicated(keep = "first")]
df_markeddown = df.to_markdown()

# display entire dataframe
# st.dataframe(df, use_container_width = True)
st.bar_chart(df, x = "agency", y = "awarded_amt")
