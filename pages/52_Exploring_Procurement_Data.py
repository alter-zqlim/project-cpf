import streamlit as st
import pandas as pd
import altair as alt
# import plotly.express as px

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
df = unsorted_df.sort_values(by = [data_input_index, "tender_no", "supplier_name", "award_date"])
df_index = df[~df.index.duplicated(keep = "first")]
df_markeddown = df.to_markdown()

# agency_list = list(df.agency.unique())[::-1]
# st.write(agency_list)

# selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
# df_selected_year = df_reshaped[df_reshaped.year == selected_year]
# df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)


# display entire dataframe
# st.dataframe(df, use_container_width = True)
# st.bar_chart(df, y = "agency", x = "awarded_amt", y_label = "Agency", x_label = "Awarded Procurement Value")
counts = df[data_input_index].value_counts().reset_index()
counts.columns = [data_input_index, "count"]
st.scatter_chart(counts.sort_values(by = "count", ascending = False), y = "agency", size = "count", y_label = "Agency", x_label = "Number of Awarded Tenders")


# password checkpoint
if not utility.check_password():  
    st.stop()

pandas_agent = llm.init_pandas_dataframe_agent(df)
csv_agent = llm.init_csv_agent("./data/GovernmentProcurementviaGeBIZ.csv")

# generate a multi-option selector that displays data based on selected agencies  
agencies = st.multiselect(
    "Select agencies",
    list(df.agency.unique())[::-1],
    # list(df_index.index),
    ["Competition and Consumer Commission of Singapore (CCCS)"]
)

col_01, col_02 = st.columns(2)

with col_01:
    # generate a radio selector that displays data based on tender status  
    tender_status_list = list(df.tender_detail_status.unique())[::-1]
    tender_status_list.append("All")
    tender_status = st.radio(
        "Filter information by tender award status",
        tender_status_list,
        len(tender_status_list) - 1
    )

with col_02:
    # generate a radio selector that displays data based on tender status
    df["year"] = pd.to_datetime(df["award_date"], format = "%d/%m/%Y")
    list_years = df["year"].dt.year.unique().tolist()
    # years = st.multiselect(
        # "Filter information by year(s) of tender awarded",
        # list_years,
        # default = list_years
    # )

# if not years:
    # st.error("Please select at least one year.")
# else:
if not agencies:
    st.error("Please select at least one agency.")
else:
    if tender_status == "All":
        # data_filtered = df.loc[agencies]
        data_filtered = df[df["agency"].isin(agencies)]
        data = data_filtered.drop(columns = ["year"])
        st.write("## Procurement projects", data.sort_index())
    else:
        data_filtered = df[(df["agency"].isin(agencies)) & (df["tender_detail_status"] == tender_status)]
        data = data_filtered.drop(columns = ["year"])
        st.write("## Procurement projects", data.sort_index())

# generate a form for user input
form = st.form(key = "form")
form.subheader("What would you like to know about the GeBiz procurement data from FY2019 to FY2023?")

user_input = form.text_area(
    "Please enter your query below and press Submit", 
    height = 160
)

# on detecting Submit, processes and writes response to user input
if form.form_submit_button("Submit"):
    st.toast(f"User Input: {user_input}")
    # response = csv_agent.invoke(llm.improved_question(user_input))
    # response = pandas_agent.invoke(llm.improved_question(user_input))
    response = pandas_agent.invoke(user_input)
    # response = llm.generate_response_based_on_procurement_data(user_input, data)  # unable to use to_markdown() because of token limit
    st.write(response)
    # st.write(response["output"])
